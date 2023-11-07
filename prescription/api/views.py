from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from prescription.models import Prescription
from .serializers import PrescriptionSerializer, PrescriptionViewSerializer

# Create your views here.

class PrescriptionGET(ListCreateAPIView):
    serializer_class = PrescriptionViewSerializer
    
    def get_queryset(self):
        return Prescription.objects.all()
    
class PrescriptionSAVE(ListCreateAPIView):
    serializer_class = PrescriptionSerializer
    def perform_create(self, serializer):
        return serializer.save()
    

class Prescriptiondetailviews(RetrieveUpdateDestroyAPIView):
    serializer_class = PrescriptionViewSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        return Prescription.objects.all()