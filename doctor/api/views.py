from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from doctor.models import Doctor
from .serializers import DoctorSerializer

# Create your views here.
class Doctorviews(ListCreateAPIView):
    serializer_class = DoctorSerializer
    def perform_create(self, serializer):
        return serializer.save()
    
    def get_queryset(self):
        return Doctor.objects.all()
    
class Doctordetailviews(RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    Doctor_field = 'id'
    
    def get_queryset(self):
        return Doctor.objects.all()