from rest_framework import serializers, status
from .models import Usuario
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response




class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=1, write_only=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol', 'idPersona', "password"]
        # extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],
            email=validated_data['email'],
            rol=validated_data['rol'],
            idPersona=validated_data['idPersona']
        )
        user.set_password(validated_data['password'])
        user.save()
        return Response({'mensaje': 'Usuario creado exitosamente'} , status=status.HTTP_201_CREATED)
    


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['rol'] = user.rol
        token['idPersona'] = user.idPersona
        return token
    
