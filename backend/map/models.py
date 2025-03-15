from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating = models.FloatField(default=0.0)  # Average rating
    cuisine_type = models.CharField(max_length=100, blank=True, null=True)  # Optional
    user_likes = models.IntegerField(default=0)  # Number of likes

    def __str__(self):
        return self.name


class RahmaRestaurant(models.Model):  # Add this model if missing
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating = models.FloatField(default=0)  # Optional: if you want to rank them

class Association(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating = models.FloatField(default=0)  # Optional
