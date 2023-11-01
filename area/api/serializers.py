from area.models import Area
from rest_framework import serializers
from hospital.api.serializers import HospitalSerializer
from entity.api.serializers import EntitySerializer

class AreaSerializer(serializers.ModelSerializer):
    entity_in_area = EntitySerializer(many=True, read_only=True)
    hospitals_in_area = HospitalSerializer(many=True, read_only=True)
    class Meta:
        model = Area
        fields = ['name', 'entity_in_area', 'hospitals_in_area']