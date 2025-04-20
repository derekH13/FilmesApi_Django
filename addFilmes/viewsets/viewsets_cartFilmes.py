from rest_framework.viewsets import ModelViewSet

from addFilmes.models.models_cartFilmes import cartFilmes
from ..serializers import CartFilmesSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view


class CartFilmesViewsets(ModelViewSet):
    # user vai ser ordenado por id
    queryset = cartFilmes.objects.all().order_by('cartFilmes_id')
    serializer_class = CartFilmesSerializer


@api_view(['GET'])
def get_CartUser(request, idUser):
    if request.method == 'GET':
        try:
            cart = cartFilmes.objects.filter(user_id=idUser)

            serializer = CartFilmesSerializer(cart, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
