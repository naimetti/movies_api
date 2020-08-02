from .models import Movie, Person
from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id',
            'first_name',
            'last_name',
            'aliases',
            'as_actor',
            'as_director',
            'as_producer',
        ]


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'release_year',
            'cast',
            'directors',
            'producers',
        ]