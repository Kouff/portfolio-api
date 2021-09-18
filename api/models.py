from django.contrib.auth.models import User
from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='portfolios', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    # images


class Image(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default='')
    portfolio = models.ForeignKey(Portfolio, related_name='images', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    # comments


class Comment(models.Model):
    text = models.TextField()
    image = models.ForeignKey(Image, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(auto_now_add=True)
