from django.shortcuts import render,get_object_or_404,redirect
from .models import Appointment
from patients.models import Patient
from doctors.models import Doctor


def schedule_appointment(request):
    if request.method == 'POST':
        patient = Patient.objects.get(id=request.POST['patient_id'])
        doctor = Doctor.objects.get(id=request.POST['doctor_id'])
        appointment = Appointment.objects.create(
            patient = patient,
            doctor = doctor,
            date = request.POST['date'],
            time = request.POST['time'],
        )
        return redirect('appointments:appointment_detail',appointment.id)
    doctors = Doctor.objects.all()
    return render(request,'appointments/schedule.html', {'doctors':doctors})

def appontment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment,pk=appointment_id)
    return render(request, 'appointments/appointment_detail.html',{'appointment':appointment})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request,'appointments/appointment_list.html',{'appointments':appointments})


    
    
        

