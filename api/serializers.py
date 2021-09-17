from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError
from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):
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
        user = User(**attrs)
        try:
            validate_password(attrs.get("password"), user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
