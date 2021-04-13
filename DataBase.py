from Ville import Ville


class FileLoader:
    def __init__(self, path):

        file = open(path, "r")
        self.lignes = file.readlines()
        file.close()

    def parse(self):

        def parseSubLignes(lignes, index):
            voisins = {}
            nbrlignes = len(lignes)

            for i in range(index + 1, nbrlignes):

                ligne = lignes[i]

                if len(ligne.split()) == 2:
                    (villeV, distance) = ligne.split()
                    voisins[villeV] = int(distance)

                elif len(ligne.split()) == 3:
                    return voisins

            return voisins

        villes = []

        for i in range(0, len(self.lignes)):
            ligne = self.lignes[i]
            if len(ligne.split()) == 3:
                (nom, lat, long) = ligne.split()
                ville = Ville(nom, lat, long)
                voisins = parseSubLignes(self.lignes, i)
                ville.voisins = voisins
                villes.append(ville)

        return villes
