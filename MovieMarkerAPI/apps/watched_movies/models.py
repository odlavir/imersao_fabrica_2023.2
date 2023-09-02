from apps.movies.models import Movie
from apps.users.models import User
from django.db import models


# Create your models here.
class WatchedMovies(models.Model):
  
  usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
  filme = models.ForeignKey(Movie, on_delete=models.CASCADE, null=False)
  comentario = models.TextField()
  nota = models.FloatField(help_text="Digite um valor de 0 à 10.")
  created_at = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.usuario} - {self.filme}"