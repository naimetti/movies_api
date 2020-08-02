from api.models import Person


def test_person_list(actors,):
    print(Person.objects.all())
