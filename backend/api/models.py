from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=20, choices=[
        ('volunteer', 'Volunteer'),
        ('organization', 'Charitable Organization'),
        ('admin', 'Admin')
    ], default='volunteer')

    def __str__(self):
        return self.username

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()

    def __str__(self):
        return self.address
    
    def get_coordinates(self):
        return (self.latitude, self.longitude)
    
    def calculate_distance(self, other_location):
        # Simplified distance calculation - in a real app, you'd use a proper geospatial library
        lat_diff = abs(self.latitude - other_location.latitude)
        long_diff = abs(self.longitude - other_location.longitude)
        return (lat_diff ** 2 + long_diff ** 2) ** 0.5

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='volunteer_profile')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Volunteer: {self.user.username}"
    
    def view_nearby_organizations(self, radius=10):
        # This would use geospatial queries in a real implementation
        if not self.location:
            return CharitableOrganization.objects.none()
        return CharitableOrganization.objects.filter(location__isnull=False)
    
    def view_history(self):
        return self.volunteer_history.all()

class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    url = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255, blank=True)
    upload_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Photo: {self.caption or self.photo_id}"
    
    def upload_photo(self, image):
        self.url = image
        self.save()
    
    def delete_photo(self):
        self.delete()

class CharitableOrganization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organization_profile')
    name = models.CharField(max_length=100)
    description = models.TextField()
    contact_info = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    photos = models.ManyToManyField(Photo, blank=True, related_name='organization_photos')
    
    def __str__(self):
        return self.name
    
    def add_photos(self, photo):
        self.photos.add(photo)
    
    def view_dashboard(self):
        # In a real implementation, this would return analytics data
        events = self.events.all()
        volunteers = [volunteer for event in events for volunteer in event.volunteers.all()]
        return {
            'total_events': events.count(),
            'active_events': events.filter(status='active').count(),
            'total_volunteers': len(set(volunteers)),
            'volunteer_requests': self.volunteer_requests.all().count()
        }

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(CharitableOrganization, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    volunteers_needed = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=[
        ('planned', 'Planned'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='planned')
    photos = models.ManyToManyField(Photo, blank=True, related_name='event_photos')
    volunteers = models.ManyToManyField(Volunteer, blank=True, related_name='events')
    
    def __str__(self):
        return self.title
    
    def create_event(self):
        self.save()
    
    def update_event(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
    
    def cancel_event(self):
        self.status = 'cancelled'
        self.save()

class VolunteerRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(CharitableOrganization, on_delete=models.CASCADE, related_name='volunteer_requests')
    description = models.TextField()
    skills = models.JSONField(default=list)
    number_of_volunteers = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=[
        ('open', 'Open'),
        ('filled', 'Filled'),
        ('closed', 'Closed')
    ], default='open')
    
    def __str__(self):
        return f"Request by {self.organization.name}: {self.number_of_volunteers} volunteers"
    
    def create_request(self):
        self.save()
    
    def update_request(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
    
    def close_request(self):
        self.status = 'closed'
        self.save()

class VolunteerHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name='volunteer_history')
    organization = models.ForeignKey(CharitableOrganization, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    donation_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    type = models.CharField(max_length=20, choices=[
        ('event', 'Event Participation'),
        ('donation', 'Donation')
    ])
    
    def __str__(self):
        if self.type == 'event':
            return f"{self.volunteer.user.username} participated in {self.event.title if self.event else 'Unknown event'}"
        else:
            return f"{self.volunteer.user.username} donated to {self.organization.name if self.organization else 'Unknown organization'}"
    
    @classmethod
    def add_history_entry(cls, volunteer, type, **kwargs):
        entry = cls(volunteer=volunteer, type=type, **kwargs)
        entry.save()
        return entry