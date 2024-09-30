# serializers.py
from rest_framework import serializers
from .models import Patient, Doctor, Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
<<<<<<< Updated upstream
=======


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
>>>>>>> Stashed changes
