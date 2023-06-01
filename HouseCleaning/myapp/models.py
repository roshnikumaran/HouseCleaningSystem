from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    profile_picture=models.ImageField(upload_to="profilepics",null=True)
    bio=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    date_of_birth=models.DateField(null=True)
    options=(
        ("male","male"),
        ("female","female"),
        ("other","other")
    )
    gender=models.CharField(max_length=15,choices=options,default="male")
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="users")

    def __str__(self):
        return self.user.username
    
class CleaningService(models.Model):
    location=models.CharField(max_length=200)
    options=("weekly","monthly")
    freequency=models.CharField(max_length=200,choices=options,default="weekly")
    work_time=models.DateTimeField(auto_now_add=True)
    options=("cleaning","cooking","plumping","washing","other")
    services=models.CharField(max_length=200,choices=options,default="cleaning")

    def __str__(self):
        return self.services
