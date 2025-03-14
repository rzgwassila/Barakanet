# serializers.py
from rest_framework import serializers
from .models import User, CharityEvent, ItemRequest, VolunteerApplication, ItemLending

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
