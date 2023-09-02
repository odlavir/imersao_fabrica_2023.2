from apps.movies.api.viewsets import MovieViewSet
from django.urls import include, path
from rest_framework import routers

# A seguir, iremos criar o endpoint para acessar os filmes.

router = routers.DefaultRouter()
router.register("", MovieViewSet, basename="movie")

urlpatterns = [
    path("", include(router.urls))
]
