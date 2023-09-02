from apps.watched_movies.models import WatchedMovies
from rest_framework.viewsets import ModelViewSet

from .serializers import WatchedMoviesSerializer

class WatchedMoviesViewSet(ModelViewSet):

  # Com essa query, irá ser buscado todos os dados da tabela abaixo:
  queryset = WatchedMovies.objects.all()  
  serializer_class = WatchedMoviesSerializer
