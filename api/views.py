from api.models import Person, Movie
from rest_framework import viewsets, filters
from rest_framework import permissions
from .serializers import PersonSerializer, MovieSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name']
    search_fields = [
        'first_name',
        'last_name',
        'aliases',
        'as_actor__title',
        'as_director__title',
        'as_producer__title',
    ]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'release_year']
    ordering_fields = ['title', 'release_year']
    search_fields = [
        'title',
        'release_year',
        'cast__first_name', 'cast__last_name',
        'directors__first_name', 'directors__last_name',
        'producers__first_name', 'producers__last_name',
    ]
