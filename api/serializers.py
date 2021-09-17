from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from api import helpers


class CreateUserSerializer(serializers.ModelSerializer):
    """ Serializer for creating a new user """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')
        read_only_fields = ('id',)
        extra_kwargs = {
            'first_name': {'default': '', 'required': False},
            'last_name': {'default': '', 'required': False},
            'email': {'default': '', 'required': False},
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        return helpers.validate_password_field(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserMeSerializer(serializers.ModelSerializer):
    """ Serializer for showing and editing the current user """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')
        read_only_fields = ('id', 'username')
        extra_kwargs = {
            'first_name': {'default': '', 'required': False},
            'last_name': {'default': '', 'required': False},
            'email': {'default': '', 'required': False},
            'password': {'write_only': True, 'required': False},
        }

    def validate(self, attrs):
        return helpers.validate_password_field(attrs)

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        if password:
            validated_data['password'] = make_password(password)
        return super().update(instance, validated_data)

