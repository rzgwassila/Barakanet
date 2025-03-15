# serializers.py
from rest_framework import serializers
from .models import User, Volunteer, Charity, CharityFile, CharityImage
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is deactivated.")
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        data['user'] = user
        return data
    
class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['qr_code']

class CharityFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharityFile
        fields = ['id', 'file', 'description', 'uploaded_at']

class CharityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharityImage
        fields = ['id', 'image', 'caption', 'uploaded_at']

class CharitySerializer(serializers.ModelSerializer):
    files = CharityFileSerializer(many=True, read_only=True)
    images = CharityImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Charity
        fields = ['social_media_linkedin', 'social_media_twitter', 
                  'social_media_facebook', 'social_media_instagram',
                  'files', 'images']

class UserSerializer(serializers.ModelSerializer):
    volunteer_profile = VolunteerSerializer(read_only=True)
    charity_profile = CharitySerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'location', 
                  'role', 'volunteer_profile', 'charity_profile']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        role = validated_data.pop('role')
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        
        if password:
            user.set_password(password)
        
        user.role = role
        user.save()
        
        # Create role-specific profile
        if role == 'volunteer':
            Volunteer.objects.create(user=user)
        elif role == 'charity':
            Charity.objects.create(user=user)
            
        return user