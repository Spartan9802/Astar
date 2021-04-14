from Ville import Ville


class Villes:
    villes = {}

    # Récupére l'instance de la class Ville par le nom dans le dictionaire
    @staticmethod
    def getVilleByName(villeName):
        villeName = str.lower(villeName)
        if villeName in Villes.villes:
            return Villes.villes[villeName]
        return

    @staticmethod
    def addVille(ville: Ville):
        name = str.lower(ville.nom)
        Villes.villes[name] = ville

    @staticmethod
    def addVilles(villes: [Ville]):
        for ville in villes:
            Villes.addVille(ville)
