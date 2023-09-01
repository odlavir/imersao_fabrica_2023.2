from rest_framework.viewsets import ModelViewSet

from apps.users.models import User
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
    
    # Busca todos os dados que estão na tabela User.
    queryset = User.objects.all()
    
    serializer_class = UserSerializer
