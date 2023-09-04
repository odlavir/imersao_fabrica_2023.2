from apps.users.models import User
from rest_framework import serializers
from apps.movie_comments.models import MovieComments


class UserSerializer(serializers.ModelSerializer):
  
  watchedMovies = serializers.SerializerMethodField()
  
  class Meta:
    model = User
    
    # Com esse fields, irá ser mostrado todos dados existentes no model.
    fields = ["id", "name", "email", "date_of_birth", "created_at", "watchedMovies"]
    db_table = 'users'
    
  def get_watchedMovies(self, obj):
    
    movies = MovieComments.objects.filter(user = obj.id)
    moviesList = []
    
    for movie in movies:
      moviesList.append(movie.movie.title)

    return moviesList
