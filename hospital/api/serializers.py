from hospital.models import Hospital
from rest_framework import  serializers
from doctor.api.serializers import DoctorSerializer

class HospitalSerializer(serializers.ModelSerializer):
    doctors = DoctorSerializer(many=True, read_only=True)
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='name')
    class Meta:
        model = Hospital
        fields = ['name','value','label', 'phones', 'doctors']