import pytest
import factory

from api.models import Person, Movie


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


@pytest.fixture
def persons(db):
    for _ in range(10):
        PersonFactory()
