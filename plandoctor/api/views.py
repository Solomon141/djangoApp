from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from plandoctor.models import PlanDoctor
from .serializers import PlanDoctorSerializer, PlanDoctor_Text_Serializer

# Create your views here.
class PlanDoctorviews(ListCreateAPIView):
    serializer_class = PlanDoctorSerializer
    def perform_create(self, serializer):
        return serializer.save()
    
    
class PlanGetDoctorviews(ListCreateAPIView):
    serializer_class = PlanDoctor_Text_Serializer
    def get_queryset(self):
        return PlanDoctor.objects.all()

class PlanDoctordetailviews(RetrieveUpdateDestroyAPIView):
    serializer_class = PlanDoctorSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        return PlanDoctor.objects.all()