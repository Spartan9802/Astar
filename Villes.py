from Ville import Ville

class Villes:

    villes = {}

    # Récupére l'instance de la class Ville par le nom dans le dictionaire
    @staticmethod
    def getVilleByName(villeName):
        if villeName in Villes.villes:
            return Villes.villes[villeName]
        return

    @staticmethod
    def addVille(ville: Ville):
        Villes.villes[ville.nom] = ville

    @staticmethod
    def addVilles(villes: [Ville]):
        for ville in villes:
            Villes.addVille(ville)
