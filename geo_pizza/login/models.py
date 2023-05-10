from django.db import models
from django.contrib.auth.models import User

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

# from django.db import models
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=100, blank = True)
#     phone_number = models.CharField(max_length=100, blank = True)
#     profile_image = models.CharField(max_length=999, blank = True)
