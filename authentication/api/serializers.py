from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework.decorators import authentication_classes, permission_classes

@authentication_classes([])
@permission_classes([])
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    # tokens = CustomTokenObtainPairSerializer()
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'groups', 'password']
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        createdUser = User.objects.create_user(**validated_data)
        return createdUser
    
    
    
@authentication_classes([])
@permission_classes([])
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'password']
        depth = 1




