from django.apps import AppConfig
from .loaders import load_data


class ConstructionDataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "construction_data"

    # Initialisation d'un attribut pour stocker les données chargées
    loaded_data = None

    def ready(self):
        # Chargement des données JSON dans un attribut de la classe au démarrage
        ConstructionDataConfig.loaded_data = load_data()
