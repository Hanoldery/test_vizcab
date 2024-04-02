from construction_data.utils import find_object_by_id


def calculate_impact_production(impact, quantite):
    """
    Calcul l'impact de la production
    """

    return impact * quantite


def calculate_impact_construction(impact, quantite):
    """
    Calcul l'impact de la construction
    """

    return impact * quantite


def calculate_impact_exploitation(
    impact, renouvellement, impact_production, impact_construction, quantite
):
    """
    Calcul l'impact de l'exploitation
    """

    impact_exploitation_unitaire = impact * renouvellement + (renouvellement - 1) * (
        impact_production + impact_construction
    )
    return impact_exploitation_unitaire * quantite


def calculate_impact_fin_de_vie(impact, quantite):
    """
    Calcul l'impact de la fin de vie
    """

    return impact * quantite


def calculate_renouvellement(periode_reference, duree_vie_typique):
    """
    Calcul l'impact du renouvellement
    """

    return max(1, periode_reference / duree_vie_typique)


def calculcate_impact_for_produit(batiment, produit, quantite):
    """
    Calcul l'impact du cycle de vie du produit
    """

    # Calcul du renouvellement
    renouvellement = calculate_renouvellement(
        batiment.periode_de_reference, produit.duree_vie_typique
    )

    # Calcul de l'impact Production
    impact_production = calculate_impact_production(
        produit.impact_unitaire["production"], quantite
    )

    # Calcul de l'impact Construction
    impact_construction = calculate_impact_construction(
        produit.impact_unitaire["construction"], quantite
    )

    # Calcul de l'impact Exploitation
    impact_exploitation = calculate_impact_exploitation(
        produit.impact_unitaire["exploitation"],
        renouvellement,
        impact_production,
        impact_construction,
        quantite,
    )

    # Calcul de l'impact Fin de vie
    impact_fin_de_vie = calculate_impact_fin_de_vie(
        produit.impact_unitaire["finDeVie"], quantite
    )

    return (
        impact_production
        + impact_construction
        + impact_exploitation
        + impact_fin_de_vie
    )


def calculate_impact_for_zone(loaded_data, batiment, zone):
    """
    Calcul l'impact du cycle de vie d'une zone
    """

    impact_carbone_zone = 0
    # Itération sur chaque élément de construction dans la zone
    for element in zone.construction_elements:
        produit = find_object_by_id(loaded_data, "construction_elements", element["id"])

        if produit is None:
            continue

        impact_carbone_zone += calculcate_impact_for_produit(
            batiment, produit, element["quantite"]
        )
    return impact_carbone_zone
