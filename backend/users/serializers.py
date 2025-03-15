from rest_framework import serializers
from .models import User, Volunteer, Charity, CharityFile, CharityImage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'location', 'phone_number']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'first_name', 
                  'last_name', 'role', 'location', 'phone_number']
        extra_kwargs = {'phone_number': {'required': False}}
    
    def validate(self, data):
        # Check if passwords match
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords don't match"})
        
        # Validate role
        if data['role'] not in [role[0] for role in User.USER_TYPES]:
            raise serializers.ValidationError({"role": "Invalid role selected"})
        
        return data
    
    def validate_email(self, value):
        # Check if email already exists
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use")
        return value

class VolunteerRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = []  # Currently no additional fields required for volunteer registration

class CharityRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = ['social_media_linkedin', 'social_media_twitter', 
                  'social_media_facebook', 'social_media_instagram']
        extra_kwargs = {
            'social_media_linkedin': {'required': False},
            'social_media_twitter': {'required': False},
            'social_media_facebook': {'required': False},
            'social_media_instagram': {'required': False}
        }
class CharityFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharityFile
        fields = ['id', 'charity', 'file', 'description', 'uploaded_at']

class CharityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharityImage
        fields = ['id', 'charity', 'image', 'caption', 'uploaded_at']

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)  # Can be username or email
    password = serializers.CharField(required=True, style={'input_type': 'password'})