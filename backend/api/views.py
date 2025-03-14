from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import (
    Location, Volunteer, CharitableOrganization, 
    Photo, Event, VolunteerRequest, VolunteerHistory
)
from .serializers import (
    UserSerializer, LocationSerializer, VolunteerSerializer,
    CharitableOrganizationSerializer, PhotoSerializer,
    EventSerializer, VolunteerRequestSerializer, VolunteerHistorySerializer
)

User = get_user_model()

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # For User objects
        if hasattr(obj, 'id') and isinstance(obj, User):
            return obj.id == request.user.id
        
        # For objects with a user field
        if hasattr(obj, 'user'):
            return obj.user == request.user
        
        # For organizational objects
        if hasattr(obj, 'organization'):
            return obj.organization.user == request.user
        
        return False

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    @action(detail=True, methods=['get'])
    def nearby_organizations(self, request, pk=None):
        volunteer = self.get_object()
        organizations = volunteer.view_nearby_organizations()
        serializer = CharitableOrganizationSerializer(organizations, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def history(self, request, pk=None):
        volunteer = self.get_object()
        history = volunteer.view_history()
        serializer = VolunteerHistorySerializer(history, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def donate(self, request, pk=None):
        volunteer = self.get_object()
        organization_id = request.data.get('organization_id')
        amount = request.data.get('amount')
        
        try:
            organization = CharitableOrganization.objects.get(id=organization_id)
            history_entry = VolunteerHistory.add_history_entry(
                volunteer=volunteer,
                type='donation',
                organization=organization,
                donation_amount=amount
            )
            serializer = VolunteerHistorySerializer(history_entry)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except CharitableOrganization.DoesNotExist:
            return Response({"error": "Organization not found"}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['post'])
    def sign_up_for_event(self, request, pk=None):
        volunteer = self.get_object()
        event_id = request.data.get('event_id')
        
        try:
            event = Event.objects.get(event_id=event_id)
            if event.status != 'active':
                return Response({"error": "Event is not active"}, status=status.HTTP_400_BAD_REQUEST)
            
            event.volunteers.add(volunteer)
            history_entry = VolunteerHistory.add_history_entry(
                volunteer=volunteer,
                type='event',
                event=event,
                organization=event.organization
            )
            serializer = VolunteerHistorySerializer(history_entry)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

class CharitableOrganizationViewSet(viewsets.ModelViewSet):
    queryset = CharitableOrganization.objects.all()
    serializer_class = CharitableOrganizationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    @action(detail=True, methods=['get'])
    def dashboard(self, request, pk=None):
        organization = self.get_object()
        return Response(organization.view_dashboard())
    
    @action(detail=True, methods=['post'])
    def add_photo(self, request, pk=None):
        organization = self.get_object()
        caption = request.data.get('caption', '')
        
        if 'image' not in request.FILES:
            return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        photo = Photo.objects.create(
            caption=caption,
            url=request.FILES['image']
        )
        organization.photos.add(photo)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        event = self.get_object()
        event.cancel_event()
        serializer = self.get_serializer(event)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def add_photo(self, request, pk=None):
        event = self.get_object()
        caption = request.data.get('caption', '')
        
        if 'image' not in request.FILES:
            return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        photo = Photo.objects.create(
            caption=caption,
            url=request.FILES['image']
        )
        event.photos.add(photo)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class VolunteerRequestViewSet(viewsets.ModelViewSet):
    queryset = VolunteerRequest.objects.all()
    serializer_class = VolunteerRequestSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    @action(detail=True, methods=['post'])
    def close(self, request, pk=None):
        volunteer_request = self.get_object()
        volunteer_request.close_request()
        serializer = self.get_serializer(volunteer_request)
        return Response(serializer.data)

class VolunteerHistoryViewSet(viewsets.ModelViewSet):
    queryset = VolunteerHistory.objects.all()
    serializer_class = VolunteerHistorySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        
        # If volunteer, show only their history
        if hasattr(user, 'volunteer_profile'):
            return queryset.filter(volunteer=user.volunteer_profile)
        
        # If organization, show history related to their events or donations
        if hasattr(user, 'organization_profile'):
            org = user.organization_profile
            return queryset.filter(organization=org)
        
        # Admin can see all
        if user.is_staff:
            return queryset
        
        return VolunteerHistory.objects.none()