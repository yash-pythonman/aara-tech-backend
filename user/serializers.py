from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer created to validate request for create new user.
    """

    class Meta:
        model = User
        fields = ("username", "email", "password")
