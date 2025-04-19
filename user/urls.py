from os.path import basename

from django.urls import path, include
from rest_framework import routers

from user import viewsets

router = routers.SimpleRouter()

# registro as rotas viewsets
router.register(r'user', viewsets.UserViewSet, basename='user')

urlpatterns = [
    # na rota principal inclui as rotas viewsets
    path('', include(router.urls)),
    path('username/<str:name>/', viewsets.get_username, name='get_username')
]
