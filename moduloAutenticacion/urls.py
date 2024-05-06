from django.urls import path, include

from .api import registrarUsuario, UserLoginView, UserLogoutView, getClientes

urlpatterns = [ path('api/registrar/', registrarUsuario.as_view(), name='registrar'),
                path('api/login/', UserLoginView.as_view(), name='login'),
                path('api/logout/', UserLogoutView.as_view(), name='logout'),
                path('api/clientes/', getClientes.as_view(), name = 'getUsuarios')
              ]