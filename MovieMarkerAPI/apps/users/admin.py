from django.contrib import admin

from .models import User

# Register your models here.

# A classe a seguir irá dar poder ao Admin para criar, modificar e deletar usuários.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  model = User
  
  fields = ["name", "email", "date_of_birth", "created_at"]
