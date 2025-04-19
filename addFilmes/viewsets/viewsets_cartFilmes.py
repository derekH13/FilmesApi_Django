from rest_framework.viewsets import ModelViewSet

from addFilmes.models.models_cartFilmes import cartFilmes
from ..serializers import CartFilmesSerializer
from rest_framework.response import Response
from rest_framework import status


class CartFilmesViewsets(ModelViewSet):
    # user vai ser ordenado por id
    queryset = cartFilmes.objects.all().order_by('cartFilmes_id')
    serializer_class = CartFilmesSerializer
