from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
# Create your models here.

class CustomUser(AbstractUser):
    address = RichTextField("address")
    position_name = models.CharField("position name", max_length=200, help_text="maximum 25 char")
    
    





