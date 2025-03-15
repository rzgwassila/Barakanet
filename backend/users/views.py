# views.py
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Volunteer, Charity, CharityFile, CharityImage
from .serializers import (UserSerializer, VolunteerSerializer, 
                          CharitySerializer, CharityFileSerializer, 
                          CharityImageSerializer)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# For admin-only endpoints 
permission_classes = [IsAdminUser]

# For user-specific endpoints
permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        if request.user.is_authenticated:
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)
        return Response({'detail': 'Not authenticated'}, 
                        status=status.HTTP_401_UNAUTHORIZED)

class CharityFileViewSet(viewsets.ModelViewSet):
    serializer_class = CharityFileSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return CharityFile.objects.filter(charity__user=self.request.user)
    
    def perform_create(self, serializer):
        try:
            charity = self.request.user.charity_profile
            serializer.save(charity=charity)
        except Charity.DoesNotExist:
            return Response({'detail': 'User is not a charity'}, 
                           status=status.HTTP_400_BAD_REQUEST)

class CharityImageViewSet(viewsets.ModelViewSet):
    serializer_class = CharityImageSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return CharityImage.objects.filter(charity__user=self.request.user)
    
    def perform_create(self, serializer):
        try:
            charity = self.request.user.charity_profile
            serializer.save(charity=charity)
        except Charity.DoesNotExist:
            return Response({'detail': 'User is not a charity'}, 
                           status=status.HTTP_400_BAD_REQUEST)