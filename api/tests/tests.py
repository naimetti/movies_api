from rest_framework.test import APIClient


def test_person_list(persons):
    client = APIClient()
    response = client.get('/persons/')
    assert len(response.json()) == 10

