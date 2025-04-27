from django.urls import path
from .import views

urlpatterns = [
    path('schedule/',views.schedule_appointment,name = 'schedule_appointment'),
    path('<int:appointment_id>/',views.appontment_detail,name = 'appontment_detail'),
    path('',views.appointment_list,name='appointment_list'),
]
