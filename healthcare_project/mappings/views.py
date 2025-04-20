import uuid
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, MappingDetailSerializer
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer


class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MappingDetailSerializer
        return PatientDoctorMappingSerializer

    @action(detail=False, methods=["get"], url_path="patient/(?P<patient_id>[^/.]+)")
    def patient_doctors(self, request, patient_id=None):
        try:
            uuid.UUID(patient_id)
        except ValueError:
            return Response(
                {"detail": "Invalid patient ID format. Must be a valid UUID."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)

        if not mappings.exists():
            return Response(
                {"detail": "No doctor mappings found for this patient."},
                status=status.HTTP_404_NOT_FOUND,
            )

        patient_data = PatientSerializer(mappings.first().patient).data

        doctors_data = []
        for mapping in mappings:
            mapping_data = MappingDetailSerializer(mapping).data
            mapping_data.pop("patient", None)
            doctors_data.append(mapping_data)

        return Response({"patient": patient_data, "doctors": doctors_data})

    @action(detail=False, methods=["get"], url_path="doctor/(?P<doctor_id>[^/.]+)")
    def doctor_patients(self, request, doctor_id=None):
        try:
            uuid.UUID(doctor_id)
        except ValueError:
            return Response(
                {"detail": "Invalid patient ID format. Must be a valid UUID."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        mappings = PatientDoctorMapping.objects.filter(doctor_id=doctor_id)

        if not mappings.exists():
            return Response(
                {"detail": "No doctor mappings found for this patient."},
                status=status.HTTP_404_NOT_FOUND,
            )
        
        doctor_data = DoctorSerializer(mappings.first().doctor).data
        patients_data = []
        for mapping in mappings:
            mapping_data = MappingDetailSerializer(mapping).data
            mapping_data.pop("patient", None)
            patients_data.append(mapping_data)

        return Response({"doctor": doctor_data, "patients": patients_data})
