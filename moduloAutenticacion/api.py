import django.urls
from .serializers import UsuarioSerializer, MyTokenObtainPairSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Usuario
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class registrarUsuario(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Usuario creado exitosamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
           

class getTOdosUsuarios(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class getBooleanCredencialesValidas(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        Usuario = authenticate(request, username = username, password=password)
        print("Usuario: ", Usuario)
        if Usuario is None:
            raise AuthenticationFailed('Credenciales inválidas')
        return Response({'mensaje': 'Credenciales válidas'}, status=status.HTTP_200_OK)