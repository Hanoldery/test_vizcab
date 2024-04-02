class ConstructionElement:
    def __init__(
        self, id, nom, unite, impactUnitaireRechauffementClimatique, dureeVieTypique
    ):
        self.id = id
        self.nom = nom
        self.unite = unite
        self.impactUnitaireRechauffementClimatique = (
            impactUnitaireRechauffementClimatique
        )
        self.dureeVieTypique = dureeVieTypique
