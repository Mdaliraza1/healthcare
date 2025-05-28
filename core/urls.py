from django.urls import path
from .views import (
    RegisterView,
    PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView,
    PatientDoctorMappingView, PatientDoctorListByPatient, PatientDoctorDelete
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),

    path('patients/', PatientListCreateView.as_view()),
    path('patients/<int:id>/', PatientDetailView.as_view()),

    path('doctors/', DoctorListCreateView.as_view()),
    path('doctors/<int:id>/', DoctorDetailView.as_view()),

    path('mappings/', PatientDoctorMappingView.as_view()),
    path('mappings/<int:patient_id>/', PatientDoctorListByPatient.as_view()),
    path('mappings/delete/<int:id>/', PatientDoctorDelete.as_view()),
]