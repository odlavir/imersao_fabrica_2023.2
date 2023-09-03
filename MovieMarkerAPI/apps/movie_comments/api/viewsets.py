from apps.movie_comments.models import MovieComments
from rest_framework.viewsets import ModelViewSet

from .serializers import MovieCommentsSerializer


class MovieCommentsViewSet(ModelViewSet):

  # Com essa query, irá ser buscado todos os dados da tabela abaixo:
  queryset = MovieComments.objects.all()  
  serializer_class = MovieCommentsSerializer
