from rest_framework import serializers
from .models import Cliente, User, Asesor



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'rol', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class ClienteSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(write_only=True)
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'direccion', 'ciudad', 'departamento', 'codigo_postal', 'pais', 'telefono', 'email', 'fecha_nacimiento', 'usuario', 'documento']

    def create(self, validated_data):
        user_data = validated_data.pop('usuario')
        user = User.objects.create_user(**user_data)
        cliente = Cliente.objects.create(usuario=user, **validated_data)
        return cliente
    
class AsesorSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(write_only=True)
    class Meta:
        model = Asesor
        fields = ['nombre', 'apellido', 'usuario']