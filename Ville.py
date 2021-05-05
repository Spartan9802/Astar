class Ville:
    def __init__(self, nom, lat, long):
        self.nom = nom
        self.lat = int(lat)
        self.long = int(long)
        self.voisins = {}
