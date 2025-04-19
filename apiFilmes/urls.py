from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
    path('cadastro/', include('user.urls'), name='user_urls'),
    path('catalogo/', include('addFilmes.urls'), name='catalogo_urls'),
    path('iteracao/', include('comentarios.urls'), name='iteracao')
]
