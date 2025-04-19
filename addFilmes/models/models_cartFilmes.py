from django.db import models

from django.contrib.auth.models import User


class cartFilmes(models.Model):
    cartFilmes_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,
                                # Define que, ao excluir o User, todos as iteraçoes associados a ele também serão excluídos.
                                on_delete=models.CASCADE,
                                # Permite que você acesse todos as cartFilmes de um usuário usando User.iteracao.all()
                                related_name='iteracao'
                                )
    apiFilme_id = models.TextField()
    cartFilmes_genero = models.TextField()
    cartFilmes_img = models.TextField()
    cartFilmes_title = models.TextField()
    cartFilmes_IMDB = models.BooleanField()
    cartFilmes_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} criado, guardou filme {self.apiFilme_id}, É do IMDB {self.cartFilmes_IMDB}, data {self.cartFilmes_data}"
