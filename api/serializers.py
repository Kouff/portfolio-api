from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from api import helpers
from api.models import *


class UserCreateSerializer(serializers.ModelSerializer):
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


class PortfolioSimpleSerializer(serializers.ModelSerializer):
    """ Serializer for showing portfolios in other serializers """

    class Meta:
        ref_name = None  # for read only in swagger
        model = Portfolio
        fields = ('id', 'name')


class ImageSerializer(serializers.ModelSerializer):
    """ Serializer for showing and creating a portfolio """
    portfolio = PortfolioSimpleSerializer(read_only=True)
    portfolio_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Image
        fields = ('id', 'name', 'description', 'portfolio_id', 'image', 'portfolio')
        read_only_fields = ('id', 'portfolio')

    def validate_portfolio_id(self, value):
        if value > 0 and Portfolio.objects.filter(
                pk=value,
                owner=self.context['request'].user
        ).exists():
            return value
        raise serializers.ValidationError('The portfolio you created with this id was not found.')


class ImageSimpleSerializer(serializers.ModelSerializer):
    """ Serializer for showing images in other serializers """

    class Meta:
        model = Image
        fields = ('id', 'name', 'description', 'image')
        read_only_fields = ('id',)


class PortfolioDetailSerializer(serializers.ModelSerializer):
    """ Serializer for showing and editing a portfolio """
    owner = UserSimpleSerializer(read_only=True)
    images = ImageSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = Portfolio
        fields = ('id', 'name', 'description', 'creation_date', 'owner', 'images')
        read_only_fields = ('id',)


class CommentCreateSerializer(serializers.ModelSerializer):
    """ Serializer for showing and creating a comment """
    author = UserSimpleSerializer(read_only=True)
    image_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'creation_date', 'author', 'image_id')
        read_only_fields = ('id',)

    def validate_image_id(self, value):
        if value > 0 and Image.objects.filter(pk=value).exists():
            return value
        raise serializers.ValidationError('The image with this id was not found.')

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    """ Serializer for showing and creating a comment """

    class Meta:
        model = Comment
        fields = ('id', 'text')
        read_only_fields = ('id',)


class ImageDetailSerializer(serializers.ModelSerializer):
    """ Serializer for showing and editing an image """
    portfolio = PortfolioSimpleSerializer(read_only=True)
    comments = CommentCreateSerializer(read_only=True, many=True)

    class Meta:
        model = Image
        fields = ('id', 'name', 'description', 'image', 'creation_date', 'portfolio', 'comments')
        read_only_fields = ('id',)
