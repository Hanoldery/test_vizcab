from django.apps import AppConfig
from .loaders import load_data


class ConstructionDataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "construction_data"

