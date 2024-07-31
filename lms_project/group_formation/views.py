from django.shortcuts import render
from .models import Apprenant, Groupe
import random


def index(request):
    context = {"groupes": None, "errors": []}

    if request.method == "POST":
        apprenants = request.POST.getlist("apprenants")
        nombre_groupes = request.POST.get("nombre_groupes")

        # Validation de l'entrée
        if not apprenants or not nombre_groupes:
            context["errors"].append("Tous les champs sont requis.")
        else:
            try:
                nombre_groupes = int(nombre_groupes)

                if nombre_groupes < 1:
                    context["errors"].append("Le nombre de groupes doit être au moins 1.")
                elif nombre_groupes > len(apprenants):
                    context["errors"].append("Le nombre de groupes ne peut pas être supérieur au nombre d'apprenants.")
                else:
                    # Suppression des groupes précédents
                    Groupe.objects.all().delete()

                    # Création des nouveaux apprenants
                    apprenants_obj = []
                    for nom_complet in apprenants:
                        try:
                            prenom, nom = nom_complet.split()
                            apprenants_obj.append(Apprenant.objects.create(nom=nom, prenom=prenom))
                        except ValueError:
                            context["errors"].append(
                                f"Le format du nom complet '{nom_complet}' est incorrect. Utilisez 'Prénom Nom'."
                            )

                    if not context["errors"]:
                        # Mélange des apprenants
                        random.shuffle(apprenants_obj)

                        # Formation des groupes
                        groupes = [Groupe.objects.create(nom=f"Groupe {i+1}") for i in range(nombre_groupes)]
                        for i, apprenant in enumerate(apprenants_obj):
                            groupes[i % nombre_groupes].apprenants.add(apprenant)

                        context["groupes"] = groupes

            except ValueError:
                context["errors"].append("Le nombre de groupes doit être un entier.")

    return render(request, "group_formation/index.html", context)
