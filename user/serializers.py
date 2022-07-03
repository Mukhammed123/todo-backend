from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  username = serializers.CharField(read_only=True)

class createUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'username',
      'email',
      'password'
      ]
    extra_kwargs = {'password': {'write_only': True }}


#     {
# "username": "test",
# "email": "test@gms.com",
# "password": "testtest"
# }
