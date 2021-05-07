from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Profile(models.Model):
    # Relationship between User Model and profile Model 
    # one to one means one can have only one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="profile_pict")

    def __str__(self):
        return f'{self.user.username} Profile'