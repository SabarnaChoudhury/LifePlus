# life_plus_services/core/views.py

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Patient, Doctor
from .serializers import PatientSerializer, DoctorSerializer

# ViewSet for Patient
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    @action(detail=True, methods=['get'])
    def detail(self, request, pk=None):
        """
        Custom action for retrieving a specific patient detail.
        """
        try:
            patient = self.get_object()
            serializer = self.get_serializer(patient)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response({'error': 'Patient not found'}, status=404)

# ViewSet for Doctor
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    @action(detail=True, methods=['get'])
    def detail(self, request, pk=None):
        """
        Custom action for retrieving a specific doctor detail.
        """
        try:
            doctor = self.get_object()
            serializer = self.get_serializer(doctor)
            return Response(serializer.data)
        except Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=404)
