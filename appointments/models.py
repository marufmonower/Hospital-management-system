from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField(blank=True,null=True)
    is_confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.date}-{self.patient.user.get_full_name()}with Dr. {self.doctor.user.get_full_name()}" 

class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment,on_delete=models.CASCADE)
    notes = models.TextField()
    prescribed_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Prescription for{self.appointment}"
