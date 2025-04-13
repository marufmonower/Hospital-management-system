from django.db import models
from accounts.models import CustomUser

class Patient(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.get_full_name()
    