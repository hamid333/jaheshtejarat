from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    codemeli = models.CharField(max_length=10, verbose_name='کد ملی',)
    mobile = models.CharField(max_length=11, verbose_name='موبایل', blank=True)
