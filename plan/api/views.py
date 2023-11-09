from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from plan.models import Plan
from .serializers import PlanSerializer
import datetime

# Create your views here.
class PlanSave(ListCreateAPIView):
    serializer_class = PlanSerializer
    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)
    
    def get_queryset(self):
        return Plan.objects.filter(created_by=self.request.user)
    

class PlanList(ListCreateAPIView):
    serializer_class = PlanSerializer
    def get_queryset(self):
        return Plan.objects.filter(created_by=self.request.user)
    
    
class Plandetailviews(RetrieveUpdateDestroyAPIView):
    serializer_class = PlanSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        return Plan.objects.all()
    

class PlanMonthly(ListCreateAPIView):
    serializer_class = PlanSerializer
    
    def get_queryset(self):
        pyear = self.kwargs['pyear']
        pmonth = self.kwargs['pmonth']
       
        dateMax = datetime.datetime(pyear, pmonth+1, 1)
        dateMin = datetime.datetime(pyear, pmonth, 1)
        return Plan.objects.filter(pdate__gte = dateMin, pdate__lt = dateMax)