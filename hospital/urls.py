# accounts/urls.py

# hospital/urls.py

from django.urls import path
from .views import patient_dashboard, doctor_dashboard
from .api_views import patient_appointments_api

urlpatterns = [
    path('patient/', patient_dashboard, name='patient_dashboard'),
    path('doctor/', doctor_dashboard, name='doctor_dashboard'),

    # API
    path('api/patient/', patient_appointments_api, name='patient_api'),
]