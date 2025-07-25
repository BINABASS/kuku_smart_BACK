from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser

class Farm(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    registration_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'farms_tb'
        verbose_name = _('Farm')
        verbose_name_plural = _('Farms')

class Farmer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'farmers_tb'
        verbose_name = _('Farmer')
        verbose_name_plural = _('Farmers')
