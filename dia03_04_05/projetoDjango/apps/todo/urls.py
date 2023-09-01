from django.urls import path, include

from rest_framework import routers

from apps.todo.api.viewsets import TaskViewSet

# Com isso aqui será criado o endpoint para as tasks
router = routers.DefaultRouter()

router.register("", TaskViewSet, basename="task")

urlpatterns = [
    path("", include(router.urls)),
]