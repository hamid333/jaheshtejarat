from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    Gender = (
        ('0', 'مرد'),
        ('1', 'زن'),
    )

    Status_Marriage = (
        ('', 'انتخاب کنید'),
        ('0', 'متاهل'),
        ('1', 'مجرد'),
    )

    age = models.PositiveIntegerField(null=True, blank=True)
    codemeli = models.CharField(max_length=10, verbose_name='کد ملی', unique=True)
    gender = models.CharField(max_length=10, choices=Gender, verbose_name='جنسیت', blank=True)
    status_marriage = models.CharField(max_length=2, choices=Status_Marriage, verbose_name='وضعیت تاهل', blank=True)
    mobile = models.CharField(max_length=11, verbose_name='موبایل', blank=True)
