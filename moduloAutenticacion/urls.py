from django.urls import path, include

from .api import registrarUsuario, MyTokenObtainPairView, getTOdosUsuarios, getBooleanCredencialesValidas
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [ path('api/registrar/', registrarUsuario.as_view(), name='registrar'),
                path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
                path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                path('api/usuarios/', getTOdosUsuarios.as_view(), name='usuarios'),
                path('api/credenciales/', getBooleanCredencialesValidas.as_view(), name='credenciales'),
              ]