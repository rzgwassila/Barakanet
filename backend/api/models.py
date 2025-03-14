from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('charity', 'Charity'),
        ('volunteer', 'Volunteer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    location = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    def __str__(self):
        return self.username

class CharityEvent(models.Model):
    charity = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    volunteers_needed = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    
    def __str__(self):
        return self.title

class ItemRequest(models.Model):
    event = models.ForeignKey(CharityEvent, on_delete=models.CASCADE, related_name='item_requests')
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    
    def __str__(self):
        return f"{self.name} for {self.event.title}"

class VolunteerApplication(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    volunteer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    event = models.ForeignKey(CharityEvent, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('volunteer', 'event')
    
    def __str__(self):
        return f"{self.volunteer.username} - {self.event.title}"

class ItemLending(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('returned', 'Returned'),
    )
    volunteer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lendings')
    item_request = models.ForeignKey(ItemRequest, on_delete=models.CASCADE, related_name='lendings')
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.volunteer.username} - {self.item_request.name}"
