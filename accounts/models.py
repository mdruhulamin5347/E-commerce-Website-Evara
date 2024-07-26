from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    username=models.CharField(max_length=50, unique=True, null=True, blank=True)
    profile_pic=models.ImageField(upload_to='media/' , default='def.jpg')
    email=models.EmailField(max_length=50, unique=True, null=True, blank=True)
    phone_number=models.TextField(max_length=50, null=True, blank=True)
    otp = models.CharField(max_length=5, null=True, blank=True)
    is_verified = models.BooleanField(default=False, null=True, blank=True)



class my_address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.TextField(max_length=50, null=True, blank=True)
    house_number = models.TextField(max_length=50, null=True, blank=True)
    road_number = models.TextField(max_length=50, null=True, blank=True)
    thana = models.TextField(max_length=50, null=True, blank=True)
    post_office = models.TextField(max_length=50, null=True, blank=True)
    phone_no=models.TextField(max_length=50, null=True, blank=True)
    town = models.TextField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username