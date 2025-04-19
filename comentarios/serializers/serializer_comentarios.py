from rest_framework import serializers

from comentarios.models import comentarios


class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = comentarios
        fields = ['comentario_id', 'user_id', 'apiFilme_id',
                  'comentario_texto', 'comentario_data', 'comentario_IMDB']

    def create(self, validated_data):
        return comentarios.objects.create(**validated_data)
