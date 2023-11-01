from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from planentity.models import PlanEntity
from . serializers import PlanEntitySerializer, PlanEntity_Text_Serializer

# Create your views here.
class PlanEntitySave(ListCreateAPIView):
    serializer_class = PlanEntitySerializer
    def perform_create(self, serializer):
        return serializer.save()
    
    
class PlanEntityGet(ListCreateAPIView):
    serializer_class = PlanEntity_Text_Serializer
    def get_queryset(self):
        return PlanEntity.objects.all()

class PlanEntitydetailviews(RetrieveUpdateDestroyAPIView):
    serializer_class = PlanEntitySerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        return PlanEntity.objects.all()