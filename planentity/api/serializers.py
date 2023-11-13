from rest_framework import serializers
from planentity.models import PlanEntity

class PlanEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanEntity
        fields = ['purpose', 'entities', 'products', 'planid']
        # read_only_fields = ['id','created_by']


class PlanEntity_Text_Serializer(serializers.ModelSerializer):
    entities = serializers.StringRelatedField()
    products = serializers.StringRelatedField()
    class Meta:
        model = PlanEntity
        fields = ['id', 'purpose', 'entities', 'products', 'planid']
        # read_only_fields = ['id','created_by']
