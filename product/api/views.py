from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from product.models import Badreg
from .serializers import BadregSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def badreg_get(request):
    data = Badreg.objects.all()
    serializer = BadregSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def badreg_save(request):
    item = BadregSerializer(data=request.data)
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

class Badregdetailviews(RetrieveUpdateDestroyAPIView):
    serializer_class = BadregSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Badreg.objects.all()