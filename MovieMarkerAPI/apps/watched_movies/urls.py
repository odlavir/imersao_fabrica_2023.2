from apps.watched_movies.api.viewsets import WatchedMoviesViewSet
from django.urls import include, path
from rest_framework import routers

# A seguir, iremos criar o endpoint para acessar os filmes assistidos.
router = routers.DefaultRouter()
router.register("", WatchedMoviesViewSet, basename="watched_movies")

urlpatterns = [
    path("", include(router.urls))
]
