from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from area.models import Area
from .serializers import AreaSerializer

# Create your views here.
class Areaviews(ListCreateAPIView):
    serializer_class = AreaSerializer
    def perform_create(self, serializer):
        return serializer.save()
    
    def get_queryset(self):
        return Area.objects.all()
    
class Areadetailviews(RetrieveUpdateDestroyAPIView):
    serializer_class = AreaSerializer
    Area_field = 'id'
    
    def get_queryset(self):
        return Area.objects.all()