from apps.movie_comments.api.viewsets import MovieCommentsViewSet
from django.urls import include, path
from rest_framework import routers

# A seguir, iremos criar o endpoint para acessar os os comentários e avaliações dos filmes assistidos.
router = routers.DefaultRouter()
router.register("", MovieCommentsViewSet, basename="movie_comments")

urlpatterns = [
    path("", include(router.urls))
]
