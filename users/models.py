from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
   photo = models.ImageField(upload_to='users/')
   phone_number = models.CharField(max_length=20, default='+996')
   GENDER =(
      ('Male', 'Male'),
      ('Female', 'Female')
   )
   gender = models.CharField(max_length=100, choices=GENDER, default='Male')
 
def __str__(self): 
    return self.username

# Create your models here.
