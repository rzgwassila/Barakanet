# serializers.py
from rest_framework import serializers
from .models import User, CharityEvent, ItemRequest, VolunteerApplication, ItemLending
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type', 'location', 'bio', 'profile_image']
        read_only_fields = ['id']

class ItemRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRequest
        fields = ['id', 'name', 'description', 'quantity']
        read_only_fields = ['id']

class CharityEventSerializer(serializers.ModelSerializer):
    item_requests = ItemRequestSerializer(many=True, read_only=True)
    
    class Meta:
        model = CharityEvent
        fields = ['id', 'charity', 'title', 'description', 'location', 'date', 
                  'created_at', 'updated_at', 'volunteers_needed', 'item_requests']
        read_only_fields = ['id', 'charity', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        user = self.context['request'].user
        if user.user_type != 'charity':
            raise serializers.ValidationError("Only charity users can create events")
        validated_data['charity'] = user
        return super().create(validated_data)

class VolunteerApplicationSerializer(serializers.ModelSerializer):
    volunteer_username = serializers.ReadOnlyField(source='volunteer.username')
    event_title = serializers.ReadOnlyField(source='event.title')
    
    class Meta:
        model = VolunteerApplication
        fields = ['id', 'volunteer', 'volunteer_username', 'event', 'event_title', 'status', 'created_at']
        read_only_fields = ['id', 'volunteer', 'volunteer_username', 'status', 'created_at']
    
    def create(self, validated_data):
        user = self.context['request'].user
        if user.user_type != 'volunteer':
            raise serializers.ValidationError("Only volunteer users can apply for events")
        validated_data['volunteer'] = user
        return super().create(validated_data)

class ItemLendingSerializer(serializers.ModelSerializer):
    volunteer_username = serializers.ReadOnlyField(source='volunteer.username')
    item_name = serializers.ReadOnlyField(source='item_request.name')
    
    class Meta:
        model = ItemLending
        fields = ['id', 'volunteer', 'volunteer_username', 'item_request', 'item_name', 'quantity', 'status', 'created_at']
        read_only_fields = ['id', 'volunteer', 'volunteer_username', 'status', 'created_at']
    
    def create(self, validated_data):
        user = self.context['request'].user
        if user.user_type != 'volunteer':
            raise serializers.ValidationError("Only volunteer users can lend items")
        validated_data['volunteer'] = user
        
        # Check if quantity is not more than needed
        item_request = validated_data['item_request']
        if validated_data['quantity'] > item_request.quantity:
            raise serializers.ValidationError(f"Requested quantity exceeds available quantity. Maximum: {item_request.quantity}")
        
        return super().create(validated_data)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'user_type', 'location', 'bio', 'profile_image')
        extra_kwargs = {
            'email': {'required': True},
            'user_type': {'required': True},
            'location': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        
        if attrs['user_type'] not in ['charity', 'volunteer']:
            raise serializers.ValidationError({"user_type": "User type must be either 'charity' or 'volunteer'."})
        
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

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