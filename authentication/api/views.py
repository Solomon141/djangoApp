from django.shortcuts import render
from .serializers import LoginSerializer, UserSerializer
from rest_framework.generics import GenericAPIView
from django.contrib import auth
from rest_framework.response import Response
from rest_framework import status
from djoser import utils

from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class LoginView(GenericAPIView):
    permission_classes = ()
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')

        user = auth.authenticate(username=username, password=password)
        if user:
            # djoser = djoser.Djoserdjoser()
            # djoser.username = username
            # djoser.password = password
            # tokens = djoser.generate_token()
            # access_token = tokens['access']
            # refresh_token = tokens['refresh']
            refresh = RefreshToken.for_user(user)
             
            auth_token =  {
    'refresh': str(refresh),
    'access': str(refresh.access_token),
}


            serializer = UserSerializer(user)
            data = {'user': serializer.data, 'token': auth_token}
            # data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)
            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
