# hospital/api_views.py

from django.http import JsonResponse
from .models import Appointment

def patient_appointments_api(request):
    patient = request.user.patient
    appointments = Appointment.objects.filter(patient=patient)

    data = []
    for a in appointments:
        data.append({
            "doctor": a.doctor.user.username,
            "date": str(a.date),
            "time": str(a.time),
            "status": a.status,
            "patient_name": a.patient_name,
            "age": a.patient_age
        })

    return JsonResponse({"appointments": data})