from django.contrib import admin

from .models import WatchedMovies

# Register your models here.

# A classe a seguir irá dar poder ao Admin para criar, modificar e deletar filmes que foram assistidos.
@admin.register(WatchedMovies)
class WatchedMoviesAdmin(admin.ModelAdmin):
  
  model = WatchedMovies
  fields='__all__'
