from os.path import basename

from django.urls import path, include
from rest_framework import routers

from comentarios import viewsets

router = routers.SimpleRouter()

router.register(r'comentarios', viewsets.ComentariosViewSets,
                basename='comentarios')

urlpatterns = [
    path('', include(router.urls)),
    path('comentarios/filme/<str:idFilme>/',
         viewsets.get_apiFilmeId, name='get_apiFilmeId')
]
