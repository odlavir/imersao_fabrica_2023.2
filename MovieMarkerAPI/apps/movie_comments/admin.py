from django.contrib import admin

from .models import MovieComments

# Register your models here.

# A classe a seguir irá dar poder ao Admin para criar, modificar e deletar os comentários e avaliações dos filmes assistidos.
@admin.register(MovieComments)
class MovieCommentsAdmin(admin.ModelAdmin):
  
  model = MovieComments
  fields = ["movie", "user", "comment", "rate", "created_at"]  
