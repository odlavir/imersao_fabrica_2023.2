from apps.movies.models import Movie
from rest_framework import serializers
from apps.movie_comments.models import MovieComments


class MovieSerializer(serializers.ModelSerializer):
  
  interation = serializers.SerializerMethodField()
  
  class Meta:  
      
    model = Movie
    
    # Com esse fields, irá ser mostrado todos dados existentes no model.
    fields = ["id", "title", "description", "release_year", "interation"]
    db_table = 'movies'
    
  def get_interation(self, obj):
    
    # Buscar a lista de comentários no banco de dados de acordo com o id do filme.
    comments = MovieComments.objects.filter(movie = obj.id)
    
    #Lista de interação que será apresentada ao buscar o filme.
    interationList = []

    #Entrando em cada comentário que existe no filme e extraindo o usuário, o comentário e a nota para gerar uma interação.
    for comment in comments:
      interation = {
        "username": comment.user.name,
        "comment": comment.comment,
        "rate": comment.rate,
      }
      # Adicionando a interação a lista de interações.
      interationList.append(interation)
      
    return interationList
    
    
