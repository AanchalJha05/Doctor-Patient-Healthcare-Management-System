
from hospital.models import Patient, Doctor, Appointment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse


@login_required
def patient_dashboard(request):
    
    patient = Patient.objects.filter(user=request.user).first()

    if not patient:
        return HttpResponse("Patient profile not found")

    doctors = Doctor.objects.all()
    appointments = Appointment.objects.filter(patient=patient)

    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        date = request.POST.get('date')
        time = request.POST.get('time')

        # SAFE doctor fetch
        doctor = Doctor.objects.filter(id=doctor_id).first()

        if not doctor:
            return HttpResponse("Invalid Doctor Selected")

        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            date=date,
            time=time,

            # snapshot
            patient_name=patient.user.username,
            patient_age=patient.age,
            patient_gender=patient.gender,
            patient_phone=patient.phone
        )

        return redirect('patient_dashboard')

    return render(request, 'hospital/patient_dashboard.html', {
        'patient': patient,
        'doctors': doctors,
        'appointments': appointments
    })


@login_required
def doctor_dashboard(request):
    
    doctor = Doctor.objects.filter(user=request.user).first()

    if not doctor:
        return HttpResponse("Doctor profile not found")

    appointments = Appointment.objects.filter(doctor=doctor)

    return render(request, 'hospital/doctor_dashboard.html', {
        'doctor': doctor,
        'appointments': appointments
    })