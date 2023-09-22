from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    name=models.CharField(max_length=255, null=True, blank=True)
    father_name = models.CharField(max_length=255, null=True, blank=True)
    address=models.CharField(max_length=255,null=True,blank=True)
    mobile_number=models.BigIntegerField(null=True,blank=True)
