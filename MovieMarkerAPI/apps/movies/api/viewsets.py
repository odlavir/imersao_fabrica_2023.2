from apps.movies.models import Movie
from rest_framework.viewsets import ModelViewSet

from .serializers import MovieSerializer


class MovieViewSet(ModelViewSet):
  
  # Com essa query, irá ser buscado todos os dados selecionados abaixo:
  queryset = Movie.objects.all()
   
  serializer_class = MovieSerializer