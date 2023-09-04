from django.contrib import admin

from .models import Movie

# Register your models here.

# A classe a seguir irá dar poder ao Admin para poder criar, modificar e deletar filmes.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
  model = Movie
  
  fields = ["id", "title", "description", "release_year", "interation"]
