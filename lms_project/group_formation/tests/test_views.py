import pytest
from django.urls import reverse
from group_formation.models import Apprenant, Groupe

@pytest.mark.django_db
def test_index_view_get(client):
    response = client.get(reverse('group_formation:index'))
    assert response.status_code == 200
    assert 'groupes' in response.context
    assert response.context['groupes'] is None

@pytest.mark.django_db
def test_index_view_post(client):
    data = {
        'apprenants': ['John Doe', 'Jane Doe'],
        'nombre_groupes': 1,
    }
    response = client.post(reverse('group_formation:index'), data)
    assert response.status_code == 200
    assert 'groupes' in response.context
    assert len(response.context['groupes']) == 1

@pytest.mark.django_db
def test_index_view_post_invalid_group_number(client):
    data = {
        'apprenants': ['John Doe', 'Jane Doe'],
        'nombre_groupes': 3,
    }
    response = client.post(reverse('group_formation:index'), data)
    assert response.status_code == 200
    assert 'errors' in response.context
    assert "Le nombre de groupes ne peut pas être supérieur au nombre d'apprenants." in response.context['errors']

@pytest.mark.django_db
def test_index_view_post_invalid_apprenant_format(client):
    data = {
        'apprenants': ['JohnDoe', 'Jane Doe'],
        'nombre_groupes': 1,
    }
    response = client.post(reverse('group_formation:index'), data)
    assert response.status_code == 200
    assert 'errors' in response.context
    assert "Le format du nom complet 'JohnDoe' est incorrect. Utilisez 'Prénom Nom'." in response.context['errors']
