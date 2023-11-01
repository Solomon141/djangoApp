from doctor.models import Doctor
from rest_framework import  serializers
# from plan.api.serializers import PlanSerializer
from plandoctor.api.serializers import PlanDoctorSerializer

class DoctorSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='FullName')
    # plans = PlanSerializer(many=True, read_only=True)
    plandoctor = PlanDoctorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Doctor
        fields = ['id', 'value', 'label', 'FullName', 'plandoctor']