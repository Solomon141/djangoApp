from rest_framework import serializers
from product.models import Badreg

class BadregSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='pname')
    class Meta:
        model = Badreg
        fields = ['id', 'pname', 'value', 'label']
