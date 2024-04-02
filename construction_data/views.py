from rest_framework.response import Response
from rest_framework.views import APIView

from construction_data.utils import load_data, find_object_by_id, get_batiment_zones
from construction_data.services.impact_calculations import calculate_impact_for_zone
from construction_data.services.meters_calculations import calculate_main_usage


class SurfaceView(APIView):
    """
    Vue pour calculer la surface d'un bâtiment donné.
    """

    def get(self, request, batiment_id):
        # Récupérer les données pré-chargées
        loaded_data = load_data()

        # Trouver le bâtiment par son ID
        batiment = find_object_by_id(loaded_data, "batiments", batiment_id)

        if not batiment:
            return Response({"error": "Bâtiment non trouvé"}, status=404)

        # Récupérer les zones d'un bâtiment
        zones = get_batiment_zones(loaded_data, batiment)

        # Calculer la surface des zones
        surface_totale = sum(zone.surface for zone in zones)

        return Response(
            {"id": batiment.id, "nom": batiment.nom, "surface_totale": surface_totale}
        )


class UsageView(APIView):
    """
    Vue pour calculer l'usage principal d'un bâtiment donné.
    """

    def get(self, request, batiment_id):
        # Récupérer les données pré-chargées
        loaded_data = load_data()

        # Trouver le bâtiment par son ID
        batiment = find_object_by_id(loaded_data, "batiments", batiment_id)

        if not batiment:
            return Response({"error": "Bâtiment non trouvé"}, status=404)

        # Récupérer les zones d'un bâtiment
        zones = get_batiment_zones(loaded_data, batiment)

        # Trouver l'usage principal (celui qui occupe la plus grande surface)
        usage_principal = calculate_main_usage(loaded_data, zones)

        return Response(
            {
                "id": batiment.id,
                "nom": batiment.nom,
                "usage_principal": usage_principal.nom,
            }
        )


class BatimentImpactCarboneView(APIView):
    """
    Vue pour calculer l'impact carbone sur le cycle de vie total d'un bâtiment donné.
    """

    def get(self, request, batiment_id):
        loaded_data = load_data()

        # Trouver le bâtiment par son ID
        batiment = next(
            (b for b in loaded_data["batiments"] if b.id == batiment_id), None
        )
        if not batiment:
            return Response({"error": "Bâtiment non trouvé"}, status=404)

        total_impact_carbone = 0

        # Calcul d'impact sur chaque zone du bâtiment
        for zone_id in batiment.zone_ids:
            zone = find_object_by_id(loaded_data, "zones", zone_id)

            if zone is None:
                continue

            total_impact_carbone += calculate_impact_for_zone(
                loaded_data, batiment, zone
            )

        return Response(
            {
                "id": batiment_id,
                "nom": batiment.nom,
                "impact_carbone_total": total_impact_carbone,
            }
        )
