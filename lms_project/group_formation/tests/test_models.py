import pytest
from group_formation.models import Apprenant, Groupe

@pytest.mark.django_db
def test_create_apprenant():
    apprenant = Apprenant.objects.create(nom="Doe", prenom="John")
    assert apprenant.nom == "Doe"
    assert apprenant.prenom == "John"

@pytest.mark.django_db
def test_create_groupe():
    groupe = Groupe.objects.create(nom="Groupe 1")
    assert groupe.nom == "Groupe 1"

@pytest.mark.django_db
def test_add_apprenant_to_groupe():
    groupe = Groupe.objects.create(nom="Groupe 1")
    apprenant = Apprenant.objects.create(nom="Doe", prenom="John")
    groupe.apprenants.add(apprenant)
    assert groupe.apprenants.count() == 1
    assert groupe.apprenants.first() == apprenant
