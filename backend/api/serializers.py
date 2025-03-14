from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (
    Location, Volunteer, CharitableOrganization, 
    Photo, Event, VolunteerRequest, VolunteerHistory
)

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'role']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'latitude', 'longitude', 'address']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo_id', 'url', 'caption', 'upload_date']

class VolunteerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    location = LocationSerializer(required=False)
    
    class Meta:
        model = Volunteer
        fields = ['id', 'user', 'location']
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['role'] = 'volunteer'
        user = UserSerializer().create(user_data)
        
        location_data = validated_data.pop('location', None)
        location = None
        if location_data:
            location = Location.objects.create(**location_data)
        
        volunteer = Volunteer.objects.create(user=user, location=location, **validated_data)
        return volunteer

class CharitableOrganizationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    location = LocationSerializer(required=False)
    photos = PhotoSerializer(many=True, read_only=True)
    
    class Meta:
        model = CharitableOrganization
        fields = ['id', 'user', 'name', 'description', 'contact_info', 'location', 'photos']
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['role'] = 'organization'
        user = UserSerializer().create(user_data)
        
        location_data = validated_data.pop('location', None)
        location = None
        if location_data:
            location = Location.objects.create(**location_data)
        
        organization = CharitableOrganization.objects.create(
            user=user, 
            location=location, 
            **validated_data
        )
        return organization

class EventSerializer(serializers.ModelSerializer):
    location = LocationSerializer(required=False)
    photos = PhotoSerializer(many=True, read_only=True)
    volunteers = VolunteerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Event
        fields = [
            'event_id', 'organization', 'title', 'description', 
            'date_time', 'location', 'volunteers_needed', 
            'status', 'photos', 'volunteers'
        ]
    
    def create(self, validated_data):
        location_data = validated_data.pop('location', None)
        location = None
        if location_data:
            location = Location.objects.create(**location_data)
        
        event = Event.objects.create(location=location, **validated_data)
        return event

class VolunteerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerRequest
        fields = [
            'request_id', 'organization', 'description', 
            'skills', 'number_of_volunteers', 'status'
        ]

class VolunteerHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerHistory
        fields = [
            'history_id', 'volunteer', 'organization', 
            'event', 'donation_amount', 'date', 'type'
        ]