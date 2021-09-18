from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from api import helpers
from api.models import *


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


class UserSerializer(serializers.ModelSerializer):
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


class UserSimpleSerializer(serializers.ModelSerializer):
    """ Serializer for showing users in other serializers """

    class Meta:
        ref_name = None  # for read only in swagger
        model = User
        fields = ('id', 'first_name', 'last_name', 'username')


class PortfolioSerializer(serializers.ModelSerializer):
    """ Serializer for showing and creating a portfolio """
    owner = UserSimpleSerializer(read_only=True)

    class Meta:
        model = Portfolio
        fields = ('id', 'name', 'description', 'owner')
        read_only_fields = ('id', 'owner')

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
