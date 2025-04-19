from rest_framework import serializers
from ..models import cartFilmes


class CartFilmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = cartFilmes
        fields = ['cartFilmes_id', 'user_id', 'apiFilme_id', 'cartFilmes_genero',
                  'cartFilmes_img', 'cartFilmes_title', 'cartFilmes_IMDB', 'cartFilmes_data']

    def create(self, validated_data):
        # cria com os dados validados
        return cartFilmes.objects.create(**validated_data)
