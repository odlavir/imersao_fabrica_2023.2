from django.db import models


# Create your models here.
class Movie(models.Model):
  
  title = models.CharField(max_length=100, unique=True)
  description = models.TextField()
  release_year = models.IntegerField()
  
  def __str__(self):
    return self.title
