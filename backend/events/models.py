
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

class Request(models.Model):
    REQUEST_TYPES = (
        ('volunteering', 'Volunteering'),
        ('borrowing', 'Borrowing'),
    )

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='requests')
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    task = models.CharField(max_length=255, blank=True, null=True)
    volunteers_needed = models.IntegerField(blank=True, null=True)
    item_to_borrow = models.CharField(max_length=255, blank=True, null=True)
    quantity_needed = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.request_type} request for {self.event.name}"