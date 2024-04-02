import json

from pathlib import Path

from .models import (
    Batiment,
    Zone,
    Usage,
    ConstructionElement,
)


BASE_DIR = Path(__file__).resolve().parent


def load_json_data(file_name):
    """
    Retourne le fichier JSON
    """

    file_path = BASE_DIR / "data" / file_name
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def dict_to_obj(object_class, key, value):
    """
    Convertit une paire clé-valeur en une instance de l'objet spécifié.
    """

    return object_class(int(key), value)


def load_data():
    """
    Charge et convertit les données du fichier JSON "usages.json" en instances de l'objet Usage.
    """

    usages = [
        dict_to_obj(Usage, key, value)
        for key, value in load_json_data("usages.json").items()
    ]
    zones = [Zone(**z) for z in load_json_data("zones.json")]
    batiments = [Batiment(**b) for b in load_json_data("batiments.json")]
    construction_elements = [
        ConstructionElement(**e) for e in load_json_data("construction_elements.json")
    ]

    return {
        "usages": usages,
        "zones": zones,
        "batiments": batiments,
        "construction_elements": construction_elements,
    }
