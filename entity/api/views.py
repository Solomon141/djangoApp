from django.shortcuts import render
from rest_framework import generics
from .serializers import EntitySerializer
from entity.models import Entity
# Create your views here.

class EntityList(generics.ListCreateAPIView):
    serializer_class = EntitySerializer
    def perform_create(self, serializer):
        return serializer.save()
    
    def get_queryset(self):
        return Entity.objects.all()
    
    
class EntityDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EntitySerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        return Entity.objects.all()