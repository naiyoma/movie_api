
from pyexpat import model
from secrets import choice
from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError


now = timezone.now()

type = [
    ('regular', 'Regular'),
    ('children', 'Children'),
    ('new', 'New_Release'),
]

genre_choices = [
    ('Action', 'Action'),
    ('Drama', 'Drama'),
    ('Romance', 'Romance'),
    ('Comedy', 'Comedy'),
    ('Horror', 'Horror')
]

popularity_choice = [
    ('low', '⭐'),
    ('medium', '⭐,⭐'),
    ('high', '⭐, ⭐, ⭐')
]

class User(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class MovieType(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Movie(models.Model):
    type = models.CharField(choices= type, max_length=60)
    title = models.CharField(max_length=60)
    genre = models.CharField(choices=genre_choices, max_length=10,default=30)
    popularity = models.CharField(choices=popularity_choice, max_length=60)

    def __str__(self):
        return self.title