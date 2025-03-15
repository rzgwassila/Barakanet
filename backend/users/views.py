# filepath: /home/camatchoo/WebDev/Dcf-hackathon/backend/users/views.py
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.db import transaction

from .models import User, Volunteer, Charity, CharityFile, CharityImage
from .serializers import (
    UserRegistrationSerializer, 
    VolunteerRegistrationSerializer,
    CharityRegistrationSerializer,
    UserLoginSerializer,
    UserSerializer,
    CharityFileSerializer,
    CharityImageSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CharityFileViewSet(viewsets.ModelViewSet):
    queryset = CharityFile.objects.all()
    serializer_class = CharityFileSerializer

class CharityImageViewSet(viewsets.ModelViewSet):
    queryset = CharityImage.objects.all()
    serializer_class = CharityImageSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """
    Register a new user (volunteer or charity) with their respective profile
    """
    user_serializer = UserRegistrationSerializer(data=request.data)
    
    if not user_serializer.is_valid():
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    user_data = user_serializer.validated_data
    role = user_data.get('role')
    
    # Additional validation based on role
    if role == 'volunteer':
        volunteer_serializer = VolunteerRegistrationSerializer(data=request.data)
        if not volunteer_serializer.is_valid():
            return Response(volunteer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif role == 'charity':
        charity_serializer = CharityRegistrationSerializer(data=request.data)
        if not charity_serializer.is_valid():
            return Response(charity_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Invalid user role"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create user and profile in a transaction
    try:
        with transaction.atomic():
            # Create user
            user = User.objects.create_user(
                username=user_data.get('username'),
                email=user_data.get('email'),
                password=user_data.get('password'),
                role=role,
                location=user_data.get('location'),
                phone_number=user_data.get('phone_number', '')
            )
            
            # Create profile based on role
            if role == 'volunteer':
                volunteer = Volunteer.objects.create(user=user)
                qr_code_url = volunteer.qr_code.url if volunteer.qr_code else None
            elif role == 'charity':
                profile_data = charity_serializer.validated_data
                Charity.objects.create(
                    user=user,
                    social_media_linkedin=profile_data.get('social_media_linkedin', ''),
                    social_media_twitter=profile_data.get('social_media_twitter', ''),
                    social_media_facebook=profile_data.get('social_media_facebook', ''),
                    social_media_instagram=profile_data.get('social_media_instagram', '')
                )
                qr_code_url = None
            
            # Create token for authentication
            token, _ = Token.objects.get_or_create(user=user)
            
            response_data = {
                'user': UserSerializer(user).data,
                'token': token.key,
                'message': f'{role.capitalize()} registration successful',
                'qr_code_url': qr_code_url
            }
            
            return Response(response_data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """
    Authenticate a user and return their token
    """
    serializer = UserLoginSerializer(data=request.data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if not user:
        # Try authenticating with email
        try:
            user_obj = User.objects.get(email=username)
            user = authenticate(username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None
    
    if not user:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    token, _ = Token.objects.get_or_create(user=user)
    
    qr_code_url = None
    if user.role == 'volunteer':
        qr_code_url = user.volunteer_profile.qr_code.url if user.volunteer_profile.qr_code else None
    
    return Response({
        'user': UserSerializer(user).data,
        'token': token.key,
        'role': user.role,
        'qr_code_url': qr_code_url
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    """
    Get the authenticated user's profile information
    """
    user = request.user
    
    return Response({
        'user': UserSerializer(user).data,
        'role': user.role
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    """
    Logout user by deleting their token
    """
    try:
        request.user.auth_token.delete()
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)