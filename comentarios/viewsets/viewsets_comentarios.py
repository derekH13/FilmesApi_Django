
from comentarios.models import comentarios
from comentarios.serializers import ComentariosSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class ComentariosViewSets(ModelViewSet):
    queryset = comentarios.objects.all().order_by('comentario_id')
    serializer_class = ComentariosSerializer

    def perform_create(self, serializer):
        serializer.save()


@api_view(['GET'])
def get_apiFilmeId(request, idFilme):
    if request.method == 'GET':
        try:
            Filme = comentarios.objects.filter(apiFilme_id=idFilme)

            serializer = ComentariosSerializer(Filme, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
