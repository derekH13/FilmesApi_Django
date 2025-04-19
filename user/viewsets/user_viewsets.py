from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User
from ..serializer import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(ModelViewSet):
    # user vai ser ordenado por id
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


@api_view(['GET'])
def get_username(request, name):
    if request.method == 'GET':
        try:
            Usuario = User.objects.get(username=name)

            serializer = UserSerializer(UserSerializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
