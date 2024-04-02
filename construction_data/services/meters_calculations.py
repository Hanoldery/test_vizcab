from construction_data.utils import find_object_by_id, get_batiment_zones


def calculate_main_usage(loaded_data, zones):
    """
    Calcul de l'usage principal
    """

    usages = {zone.usage: 0 for zone in zones}

    for zone in zones:
        usages[zone.usage] += zone.surface
    usage_principal_id = max(usages, key=usages.get)

    return find_object_by_id(loaded_data, "usages", usage_principal_id)


def calculate_surface(loaded_data, batiment):
    """
    Calcul de la surface totale des
    zones d'un batiment donné
    """

    # Récupérer les zones d'un bâtiment
    zones = get_batiment_zones(loaded_data, batiment)

    # Calculer la surface des zones
    return sum(zone.surface for zone in zones)