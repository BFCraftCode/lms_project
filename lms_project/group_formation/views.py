import logging
from django.db import connection, OperationalError
from django.db.migrations.executor import MigrationExecutor
from django.db import connections
from django.shortcuts import render
from .models import Apprenant, Groupe
import random

logger = logging.getLogger(__name__)


def apply_migrations():
    executor = MigrationExecutor(connections['default'])
    targets = executor.loader.graph.leaf_nodes()
    executor.migrate(targets)


def index(request):
    context = {"groupes": None, "errors": []}

    try:
        # Check if the table exists
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 FROM group_formation_groupe LIMIT 1")
        logger.info("La table group_formation_groupe existe.")
    except OperationalError:
        # If the table does not exist, apply migrations
        logger.warning("La table group_formation_groupe n'existe pas. Application des migrations.")
        apply_migrations()

    if request.method == "POST":
        apprenants = request.POST.getlist("apprenants")
        nombre_groupes = request.POST.get("nombre_groupes")

        logger.debug(f"Requête POST reçue avec {len(apprenants)} apprenants et {nombre_groupes} groupes demandés.")

        # Validation de l'entrée
        if not apprenants or not nombre_groupes:
            context["errors"].append("Tous les champs sont requis.")
            logger.warning("Validation échouée: champs requis manquants.")
        else:
            try:
                nombre_groupes = int(nombre_groupes)

                if nombre_groupes < 1:
                    context["errors"].append("Le nombre de groupes doit être au moins 1.")
                    logger.warning(f"Validation échouée: nombre de groupes invalide ({nombre_groupes}).")
                elif nombre_groupes > len(apprenants):
                    context["errors"].append("Le nombre de groupes ne peut pas être supérieur au nombre d'apprenants.")
                    logger.warning(
                        f"Validation échouée: nombre de groupes ({nombre_groupes}) supérieur au nombre d'apprenants ({len(apprenants)}).")
                else:
                    # Suppression des groupes précédents
                    Groupe.objects.all().delete()
                    logger.info("Groupes précédents supprimés.")

                    # Création des nouveaux apprenants
                    apprenants_obj = []
                    for nom_complet in apprenants:
                        try:
                            prenom, nom = nom_complet.split()
                            apprenants_obj.append(Apprenant.objects.create(nom=nom, prenom=prenom))
                        except ValueError:
                            error_message = f"Le format du nom complet '{nom_complet}' est incorrect. Utilisez 'Prénom Nom'."
                            context["errors"].append(error_message)
                            logger.error(error_message)

                    if not context["errors"]:
                        # Mélange des apprenants
                        random.shuffle(apprenants_obj)
                        logger.info("Apprenants mélangés.")

                        # Formation des groupes
                        groupes = [Groupe.objects.create(nom=f"Groupe {i+1}") for i in range(nombre_groupes)]
                        for i, apprenant in enumerate(apprenants_obj):
                            groupes[i % nombre_groupes].apprenants.add(apprenant)
                        logger.info("Groupes formés et apprenants assignés.")

                        context["groupes"] = groupes

            except ValueError as ve:
                context["errors"].append("Le nombre de groupes doit être un entier.")
                logger.error(f"Erreur de conversion: {ve}")

    return render(request, "group_formation/index.html", context)
