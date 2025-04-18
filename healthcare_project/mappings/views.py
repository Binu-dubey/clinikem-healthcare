from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, MappingDetailSerializer
# from patients.models import Patient
# from doctors.models import Doctor

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.all()

    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def patient_doctors(self, request, patient_id=None):
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        serializer = MappingDetailSerializer(mappings, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='doctor/(?P<doctor_id>[^/.]+)')
    def doctor_patients(self, request, doctor_id=None):
        mappings = PatientDoctorMapping.objects.filter(doctor_id=doctor_id)
        serializer = MappingDetailSerializer(mappings, many=True)
        return Response(serializer.data)