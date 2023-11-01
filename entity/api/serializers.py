from rest_framework import serializers
from entity.models import Entity, ContactPerson
from plan.api.serializers import PlanSerializer


class ContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPerson
        fields = '__all__'
        depth = 1

class EntitySerializer(serializers.ModelSerializer):
    planentity = PlanSerializer(many=True, read_only=True)
    class Meta:
        model = Entity
        fields = '__all__'
        depth = 1