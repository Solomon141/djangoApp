from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from hospital.models import Hospital
from .serializers import HospitalSerializer

# Create your views here.
class Hospitalviews(ListCreateAPIView):
    serializer_class = HospitalSerializer
    def perform_create(self, serializer):
        return serializer.save()
    
    def get_queryset(self):
        return Hospital.objects.all()
    
class Hospitaldetailviews(RetrieveUpdateDestroyAPIView):
    serializer_class = HospitalSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        return Hospital.objects.all()