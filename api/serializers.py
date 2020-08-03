import roman

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
            'url',
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
            'url',
        ]

    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = super().to_representation(instance)
        ret['release_year'] = roman.toRoman(ret['release_year'])
        return ret
