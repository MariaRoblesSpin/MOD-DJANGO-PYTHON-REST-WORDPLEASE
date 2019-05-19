from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=105)
    body = models.CharField(max_length=500)
    url = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    fecha_publicacion = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
