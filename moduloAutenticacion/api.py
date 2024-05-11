from .models import User, Cliente
from .serializers import UserSerializer, ClienteSerializer, AsesorSerializer
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

class registrarUsuario(APIView):
    def post(self, request):
        rol = request.data.get('usuario')['rol']
        if rol == None:
            return Response({'mensaje': 'El rol es requerido'}, status=status.HTTP_400_BAD_REQUEST)

        if rol == 'cliente':
            serializer = ClienteSerializer(data=request.data)
        elif rol == 'asesor':
            serializer = AsesorSerializer(data=request.data)
        else:
            return Response({'mensaje': 'El rol es inválido'}, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class getClientes(APIView):
    def get(self, request):
        clientes = Cliente.objects.filter()
        print(request.user.cliente)
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)
    

    


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        usuario= request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username = usuario, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.delete()  # Delete the token if it was already created
                token = Token.objects.create(user=user)
                
            response_data = {
                'token': token.key,
                'usuario': user.username,
                'rol': user.rol,
            }
            return Response(response_data)
        else:
            return Response({'mensaje': 'Usuario o contraseña invalidos'}, status=status.HTTP_401_UNAUTHORIZED)
        
class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        print(request.headers) 
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()
        return Response({'detalle': 'Salida de sesión exitosa '})
    

class obtenerRol(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        return Response({'rol': user.role}, status=status.HTTP_200_OK)