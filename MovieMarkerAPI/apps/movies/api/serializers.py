from apps.movies.models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
  class Meta:  
      
    model = Movie
    
    # Com esse fields, irá ser mostrado todos dados existentes no model.
    fields='__all__'
    db_table = 'movies'
    
