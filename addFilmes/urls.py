from os.path import basename

from django.urls import path, include
from rest_framework import routers

from addFilmes import viewsets

router = routers.SimpleRouter()

# registro as rotas viewsets
router.register(r'Filmes', viewsets.CartFilmesViewsets, basename='catalogo')

urlpatterns = [
    # na rota principal inclui as rotas viewsets
    path('', include(router.urls)),

]
