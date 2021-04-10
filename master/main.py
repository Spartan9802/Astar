import time


class Ville:
    def __init__(self, nom, lat, long):
        self.nom = nom
        self.lat = int(lat)
        self.long = int(long)
        self.voisins = {}


def analyser(lignes, index):
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


def charger(dicVilles, file):
    file = open(file, "r")
    lignes = file.readlines()
    file.close()

    for i in range(0, len(lignes)):
        l = lignes[i]
        if len(l.split()) == 3:
            (nom, lat, long) = l.split()
            ville = Ville(nom, lat, long)
            dicVilles.update({ville.nom: ville})
            voisins = analyser(lignes, i)
            ville.voisins = voisins


dictionnaireVilles = {}
charger(dictionnaireVilles, "./FRANCE.MAP")
print(dictionnaireVilles)
print(dictionnaireVilles["Calais"].voisins)

a = "Rennes"
b = "Moulins"
villeDepart = a
villeArriver = b


def distanceBeetwen(loc1, loc2):
    result = abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])
    return result / 4


def getVilleByName(villeName):
    return dictionnaireVilles[villeName]


def sortByLowest(voisins, ville):
    def sortByDistance(item1):
        item1 = getVilleByName(item1[0])
        distance = distanceBeetwen([ville.lat, ville.long], [item1.lat, item1.long])
        return distance

    return {k: v for k, v in sorted(voisins.items(), key=sortByDistance)}


def shortestRoute(start, end):
    global count
    count = 0

    villeDepart = getVilleByName(start)
    villeArriver = getVilleByName(end)
    global minWeight, path
    minWeight = None
    path = []

    def explore(villeName, weight, parents=[]):
        global count, minWeight, path
        count += 1
        ville = getVilleByName(villeName)
        voisins = sortByLowest(ville.voisins, villeArriver)

        if ville.nom in closedList:
            return
        closedList.append(ville.nom)
        parents.append(ville.nom)

        # print(count)
        # print("Ville Actuelle = ", ville.nom, "Ville Poids = ", weight)
        # print("Voisins = ", voisins)
        # print("Parents = ", parents)
        # print("Poids le plus court", minWeight)

        for k, v in voisins.items():

            if minWeight is not None and minWeight < (weight + v):
                continue

            if k == villeDepart.nom:
                continue

            if k == end:
                minWeight = weight + v
                path = parents.copy()
                # print("Found = ", minWeight, k)


            elif k is not end and k not in parents:
                # print("       EXPLORE")
                # print("----------------------")
                # print(weight + v, k)
                explore(k, weight + v, parents.copy())

    voisins = sortByLowest(villeDepart.voisins, villeArriver)
    for k, v in voisins.items():
        closedList = []
        if k == end:
            return
        else:
            # print("Start", k)
            explore(k, v, [])

    print(count)
    print(path, minWeight)


start = time.time()
shortestRoute(villeDepart, villeArriver)
end = time.time()
print(end - start)

