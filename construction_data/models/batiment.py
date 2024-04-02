class Batiment:
    def __init__(self, id, nom, surface, zoneIds, usage, periodeDeReference):
        self.id = id
        self.nom = nom
        self.surface = surface
        self.zone_ids = zoneIds
        self.usage = usage
        self.periode_de_reference = periodeDeReference
