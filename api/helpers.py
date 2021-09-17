from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from rest_framework import serializers


def validate_password_field(attrs):
    user = User(**attrs)
    password = attrs.get('password')
    if password is not None:
        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )
    return attrs
