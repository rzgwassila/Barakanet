from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import uuid
import qrcode # pip install qrcode[pil]
from io import BytesIO
from django.core.files import File
from PIL import Image

class User(AbstractUser):
    USER_TYPES = (
        ('volunteer', 'Volunteer'),
        ('charity', 'Charity'),
    )
    
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=10, choices=USER_TYPES)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='volunteer_profile')
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Generate QR code if it doesn't exist
        if not self.qr_code:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            # Add user info to QR code
            data = {
                'username': self.user.username,
                'email': self.user.email,
                'location': self.user.location,
                'id': str(self.user.id)
            }
            qr.add_data(str(data))
            qr.make(fit=True)
            
            # Create QR code image
            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            self.qr_code.save(f'qr_{self.user.username}.png', 
                             File(buffer), save=False)
        
        super().save(*args, **kwargs)

class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='charity_profile')
    social_media_linkedin = models.URLField(blank=True)
    social_media_twitter = models.URLField(blank=True)
    social_media_facebook = models.URLField(blank=True)
    social_media_instagram = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.user.username} Charity"

class CharityFile(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='charity_files/')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.charity.user.username} - {self.description}"

class CharityImage(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='charity_images/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.charity.user.username} - {self.caption}"