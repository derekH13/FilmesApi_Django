from django.db import models
from django.contrib.auth.models import User


class comentarios(models.Model):
    comentario_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,
                                # Define que, ao excluir o User, todos as iteraçoes associados a ele também serão excluídos.
                                on_delete=models.CASCADE,
                                related_name='comentarios'
                                )
    apiFilme_id = models.TextField()
    comentario_texto = models.TextField()
    comentario_data = models.DateField(auto_now_add=True)
    comentario_IMDB = models.BooleanField()

    def __str__(self):
        return f"usuario {self.user_id}, comentou {self.comentario_texto} no filme {self.apiFilme_id}"
