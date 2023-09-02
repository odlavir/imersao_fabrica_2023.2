from django.db import models


# Create your models here.
class User(models.Model):
  
  nome = models.CharField(max_length=200)
  email = models.EmailField(unique=True)
  data_de_nascimento = models.DateField()
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.nome
  

