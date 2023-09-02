from apps.users.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    
    # Com esse fields, irá ser mostrado todos dados existentes no model.
    fields = "__all__"    
    db_table = 'users'
    