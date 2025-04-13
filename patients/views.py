from django.shortcuts import render,get_object_or_404
from .models import Patient

def patient_list(request):
    patients = Patient.objects.all()
    return render(request,'patients/patient_list.html',{'patient':patients})

def patient_detail(request,patient_id):
    patient = get_object_or_404(Patient,pk=patient_id)
    return render(request,'patients/patient_detail.html',{'patient':patient})

    
