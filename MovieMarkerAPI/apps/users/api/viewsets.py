from apps.users.models import User
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
  
  # Com essa query, irá ser buscado todos os dados selecionados abaixo:
  queryset = User.objects.all()
  
  serializer_class = UserSerializer