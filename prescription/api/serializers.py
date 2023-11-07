from doctor.models import Doctor
from rest_framework import  serializers
from prescription.models import Prescription

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class PrescriptionViewSerializer(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField(read_only=True)
    product = serializers.StringRelatedField(read_only=True)
    created_by = serializers.StringRelatedField(read_only=True) 
    class Meta:
        model = Prescription
        fields = '__all__'