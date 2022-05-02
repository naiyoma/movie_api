from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, MovieTypeSerializer, MovieSerializer
from .models import User, MovieType, Movie


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class MovieTypeViewSet(viewsets.ModelViewSet):
    queryset = MovieType.objects.all()
    serializer_class = MovieTypeSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
