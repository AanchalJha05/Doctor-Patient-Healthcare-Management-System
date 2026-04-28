# hospital/models.py

from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100,default="medicine")
    experience = models.IntegerField(default=0,db_default=5)
    gender = models.CharField(max_length=10,default="other")
    phone = models.CharField(max_length=15,default="00000000")

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null = True,blank =True )
    gender = models.CharField(max_length=10,default="other")
    phone = models.CharField(max_length=15, default="0000000000")
    

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default="10:00")

    
    patient_name = models.CharField(max_length=100,default="Unknown")
    
    patient_age = models.IntegerField(default=0)
    patient_gender = models.CharField(max_length=10, default="Male")
    patient_phone = models.CharField(max_length=15, default="0000000000")
    

    status = models.CharField(max_length=10, default='Pending')
