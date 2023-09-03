from apps.movie_comments.models import MovieComments
from rest_framework import serializers


class MovieCommentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = MovieComments
    
    # Com esse fields, irá ser mostrado todos dados existentes no model.
    fields = "__all__"    
    db_table = 'moviecomments'