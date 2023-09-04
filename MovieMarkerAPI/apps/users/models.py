from django.db import models


# Create your models here.
class User(models.Model):
  
  name = models.CharField(max_length=200)
  email = models.EmailField(unique=True)
  date_of_birth = models.DateField()
  created_at = models.DateField(auto_now_add=True)
  

  def __str__(self):
    return self.name
  

