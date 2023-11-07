from rest_framework import serializers
from product.models import Badreg

class BadregSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badreg
        fields = ['id', 'pname']
