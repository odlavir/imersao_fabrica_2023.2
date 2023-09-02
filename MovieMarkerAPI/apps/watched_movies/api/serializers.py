from apps.watched_movies.models import WatchedMovies
from rest_framework import serializers


class WatchedMoviesSerializer(serializers.ModelSerializer):
  class Meta:
    model = WatchedMovies
    
    # Com esse fields, irá ser mostrado todos dados existentes no model.
    fields = "__all__"    
    db_table = 'watchedmovies'