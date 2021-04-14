from Ville import Ville


class Villes:
    villes = {}

    # Vérifie si la ville existe
    @staticmethod
    def villeExist(name):
        return str(name).lower() in Villes.villes

    # Récupére l'instance de la class Ville par le nom dans le dictionaire
    @staticmethod
    def getVilleByName(villeName):
        villeName = str.lower(villeName)
        if villeName in Villes.villes:
            return Villes.villes[villeName]
        return

    # Ajoute une ville
    @staticmethod
    def addVille(ville: Ville):
        name = str.lower(ville.nom)
        Villes.villes[name] = ville

    # Ajoute une liste de villes
    @staticmethod
    def addVilles(villes: [Ville]):
        for ville in villes:
            Villes.addVille(ville)
