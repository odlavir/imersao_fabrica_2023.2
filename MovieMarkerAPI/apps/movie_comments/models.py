from apps.movies.models import Movie
from apps.users.models import User
from django.db import models


# Create your models here.
class MovieComments(models.Model):
  
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
  comment = models.TextField()
  rate = models.FloatField(help_text="Enter a number from 0 to 10.")
  created_at = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.user} - {self.movie}"