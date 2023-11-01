from rest_framework import serializers
from plan.models import Plan
from plandoctor.api.serializers import PlanDoctor_Text_Serializer

class PlanSerializer(serializers.ModelSerializer):
    plandoctor = PlanDoctor_Text_Serializer(many=True, read_only=True)
    class Meta:
        model = Plan
        fields = '__all__'
        read_only_fields = ['id', 'created_by']
