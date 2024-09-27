from rest_framework import viewsets
from .models import Patient, Doctor
from .serializers import PatientSerializer, DoctorSerializer

# ViewSet for Patient
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# ViewSet for Doctor
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
