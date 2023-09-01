from django.urls import path, include

from rest_framework import routers

from apps.users.api.viewsets import UserViewSet

# Com isso aqui será criado o endpoint para os usuários.
router = routers.DefaultRouter()

router.register("", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
]