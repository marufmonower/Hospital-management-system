from django.db import models
from accounts.models import CustomUser

class Doctor (models.Model):
    user = models.OneToOneField(CustomUser,on_delete = models.CASCADE),
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    available_days = models.CharField(max_length=100)
    is_available = models.BooleanField(default = True)
    
    def __str__(self):
        return f"Dr.{self.user.get_full_name()}-{self.specialization}"

