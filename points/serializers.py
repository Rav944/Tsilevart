from django.core.validators import MinValueValidator
from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    points = serializers.IntegerField(default=0, validators=[MinValueValidator(0)])


class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    username = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    profile = ProfileSerializer()


