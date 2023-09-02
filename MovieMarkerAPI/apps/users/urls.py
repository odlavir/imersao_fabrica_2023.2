from apps.users.api.viewsets import UserViewSet
from django.urls import include, path
from rest_framework import routers

# A seguir, iremos criar o endpoint para acessar os usuários.
router = routers.DefaultRouter()
router.register("", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls))
]
