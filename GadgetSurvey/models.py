from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Gadget_Survey(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    currentMobile = models.CharField(max_length=100, blank=False)
    current_Laptop_Pc = models.CharField(max_length=100, blank=False)
    likes_device = models.IntegerField(blank=False, null=False, default=-1)
    likes_device_description = models.TextField(blank=False, null=False)
    future_device = models.IntegerField(blank=False, null=False, default=-1)
    future_device_description = models.TextField(blank=False, null=False)
