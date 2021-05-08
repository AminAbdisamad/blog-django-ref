from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    # Relationship between User Model and profile Model 
    # one to one means one can have only one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="profile_pict")

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            default_size = (300,300)
            img.thumbnail(default_size)
            img.save(self.image.path)