from django.db import models


# Create your models here.
class Movie(models.Model):
  
  titulo = models.CharField(max_length=100)
  descricao = models.TextField()
  ano_de_lancamento = models.IntegerField()
  
  def __str__(self):
    return self.titulo
