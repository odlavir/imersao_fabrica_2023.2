from apps.movie_comments.models import MovieComments
from rest_framework import serializers
from apps.movies.models import Movie
from apps.users.models import User


class MovieCommentsSerializer(serializers.ModelSerializer):
  movie = serializers.SlugRelatedField(queryset=Movie.objects.all(), slug_field="title")
  user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field="name")
  
  class Meta:
    model = MovieComments
    
    # Com esse fields, irá ser mostrado todos dados existentes no model.
    fields = ["movie", "user", "comment", "rate", "created_at"]  
    db_table = 'moviecomments'