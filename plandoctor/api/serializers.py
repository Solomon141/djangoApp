from rest_framework import serializers
from plandoctor.models import PlanDoctor
from doctor.models import Doctor

class PlanDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanDoctor
        fields = ['purpose', 'doctors', 'products', 'planid']


class PlanDoctor_Text_Serializer(serializers.ModelSerializer):
    doctors = serializers.StringRelatedField()
    products = serializers.StringRelatedField()
    class Meta:
        model = PlanDoctor
        fields = ['purpose', 'doctors', 'products', 'planid']
        # read_only_fields = ['id','created_by']
