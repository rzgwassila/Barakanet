from django.db import models
from users.models import Charity

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(Charity, on_delete=models.CASCADE, related_name='events')
    images = models.ImageField(upload_to='event_images/', blank=True, null=True)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name