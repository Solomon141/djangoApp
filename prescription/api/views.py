from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from prescription.models import Prescription
from .serializers import PrescriptionSerializer, PrescriptionViewSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class PrescriptionGET(ListCreateAPIView):
    serializer_class = PrescriptionViewSerializer
    def get_queryset(self):
        return Prescription.objects.all()
    
class PrescriptionSAVE(ListCreateAPIView):
    serializer_class = PrescriptionSerializer
    def perform_create(self, serializer):
        return serializer.save()


@api_view(['GET'])
def prescription_get(request):
    data = Prescription.objects.all()
    serializer = PrescriptionViewSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def prescription_save(request):
    item = PrescriptionSerializer(data=request.data)
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

class Prescriptiondetailviews(RetrieveUpdateDestroyAPIView):
    serializer_class = PrescriptionViewSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Prescription.objects.all()