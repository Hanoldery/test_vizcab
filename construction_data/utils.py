from django.apps import apps


def load_data():
    """
    Charge et retourne les données pré-chargées de l'application.
    """

    app_config = apps.get_app_config("construction_data")
    return app_config.loaded_data


def find_object_by_id(loaded_data, object_name, object_id):
    """
    Recherche et retourne un objet spécifique par son ID.
    """

    for obj in loaded_data[object_name]:
        if obj.id == object_id:
            return obj


def get_batiment_zones(loaded_data, batiment):
    """
    Récupère et retourne toutes les zones appartenant à un bâtiment spécifié.
    """

    zones = []

    for zone in loaded_data["zones"]:
        if zone.id in batiment.zoneIds:
            zones.append(zone)

    return zones
