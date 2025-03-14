from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import User, CharityEvent, ItemRequest, VolunteerApplication, ItemLending
from .serializers import (UserSerializer, CharityEventSerializer, ItemRequestSerializer,
                         VolunteerApplicationSerializer, ItemLendingSerializer)

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.charity == request.user

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = User.objects.all()
        user_type = self.request.query_params.get('user_type', None)
        if user_type:
            queryset = queryset.filter(user_type=user_type)
        return queryset

class CharityEventViewSet(viewsets.ModelViewSet):
    queryset = CharityEvent.objects.all()
    serializer_class = CharityEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'location']
    
    def get_queryset(self):
        queryset = CharityEvent.objects.all()
        location = self.request.query_params.get('location', None)
        if location:
            queryset = queryset.filter(location__icontains=location)
        return queryset
    
    @action(detail=True, methods=['post'])
    def add_item_request(self, request, pk=None):
        event = self.get_object()
        
        if request.user != event.charity:
            return Response({"detail": "Only the charity that created this event can add item requests"},
                           status=status.HTTP_403_FORBIDDEN)
        
        serializer = ItemRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(event=event)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemRequestViewSet(viewsets.ModelViewSet):
    queryset = ItemRequest.objects.all()
    serializer_class = ItemRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()
    
    def check_permissions(self, request):
        super().check_permissions(request)
        if self.action in ['update', 'partial_update', 'destroy']:
            obj = self.get_object()
            if request.user != obj.event.charity:
                self.permission_denied(request, message="You do not have permission to modify this item request")

class VolunteerApplicationViewSet(viewsets.ModelViewSet):
    queryset = VolunteerApplication.objects.all()
    serializer_class = VolunteerApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'charity':
            # Charities see applications to their events
            return VolunteerApplication.objects.filter(event__charity=user)
        else:
            # Volunteers see their own applications
            return VolunteerApplication.objects.filter(volunteer=user)
    
    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        application = self.get_object()
        
        if request.user != application.event.charity:
            return Response({"detail": "Only the charity that created this event can update application status"},
                           status=status.HTTP_403_FORBIDDEN)
        
        new_status = request.data.get('status')
        if new_status not in ['accepted', 'rejected']:
            return Response({"detail": "Status must be 'accepted' or 'rejected'"},
                           status=status.HTTP_400_BAD_REQUEST)
        
        application.status = new_status
        application.save()
        
        return Response(VolunteerApplicationSerializer(application).data)

class ItemLendingViewSet(viewsets.ModelViewSet):
    queryset = ItemLending.objects.all()
    serializer_class = ItemLendingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'charity':
            # Charities see lendings to their events
            return ItemLending.objects.filter(item_request__event__charity=user)
        else:
            # Volunteers see their own lendings
            return ItemLending.objects.filter(volunteer=user)
    
    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        lending = self.get_object()
        
        if request.user != lending.item_request.event.charity:
            return Response({"detail": "Only the charity that created this event can update lending status"},
                           status=status.HTTP_403_FORBIDDEN)
        
        new_status = request.data.get('status')
        if new_status not in ['accepted', 'rejected', 'returned']:
            return Response({"detail": "Status must be 'accepted', 'rejected', or 'returned'"},
                           status=status.HTTP_400_BAD_REQUEST)
        
        lending.status = new_status
        lending.save()
        
        return Response(ItemLendingSerializer(lending).data)
