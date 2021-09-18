from django.contrib.auth.models import User
from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='portfolios', on_delete=models.CASCADE)
    # images


class Image(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    portfolio = models.ForeignKey(Portfolio, related_name='images', on_delete=models.CASCADE)
    # comments


class Comment(models.Model):
    text = models.TextField()
    image = models.ForeignKey(Portfolio, related_name='comments', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
