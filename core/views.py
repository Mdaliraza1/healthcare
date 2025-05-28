from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Patient, Doctor, PatientDoctor
from .serializers import (
    RegisterSerializer, PatientSerializer, DoctorSerializer, PatientDoctorSerializer
)
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class PatientDoctorMappingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PatientDoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        mappings = PatientDoctor.objects.all()
        serializer = PatientDoctorSerializer(mappings, many=True)
        return Response(serializer.data)

class PatientDoctorListByPatient(APIView):
    def get(self, request, patient_id):
        mappings = PatientDoctor.objects.filter(patient_id=patient_id)
        serializer = PatientDoctorSerializer(mappings, many=True)
        return Response(serializer.data)

class PatientDoctorDelete(APIView):
    def delete(self, request, id):
        mapping = get_object_or_404(PatientDoctor, id=id)
        mapping.delete()
        return Response({'message': 'Mapping deleted'})
