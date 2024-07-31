from django.db import models


class Apprenant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Groupe(models.Model):
    nom = models.CharField(max_length=100)
    apprenants = models.ManyToManyField(Apprenant)

    def __str__(self):
        return self.nom
