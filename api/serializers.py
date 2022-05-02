from rest_framework import serializers

from .models import User, MovieType, Movie

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'alias')



class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'type',
            'title',
            'genre',
            'popularity',
        )
        

class MovieTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieType
        fields = (
            'reqular'
        )
