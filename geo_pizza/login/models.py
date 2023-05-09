from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    profile_image = models.CharField(max_length=999, default='https://www.pngitem.com/pimgs/m/30-307416_profile-icon-png-image-free-download-searchpng-employee.png')

class User_phonenr(User):
    phone_number = PhoneNumberField()


# from django.db import models
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=100, blank = True)
#     phone_number = models.CharField(max_length=100, blank = True)
#     profile_image = models.CharField(max_length=999, blank = True)
