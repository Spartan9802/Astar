import time
from DataBase import FileLoader
from Villes import Villes

fileLoader = FileLoader("../FRANCE.MAP")
Villes.addVilles(fileLoader.parse())

# Récupére la distance entre deux positions
def distanceBetween(loc1, loc2):
    result = abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])
    return result / 4


# Trie les voisins du plus petit au plus grand en fonction de leurs distance avec l'arrivé
def sortByLowest(voisins, ville):
    def sortByDistance(item):
        item = Villes.getVilleByName(item[0])
        distance = distanceBetween([ville.lat, ville.long], [item.lat, item.long])
        return distance

    return {k: v for k, v in sorted(voisins.items(), key=sortByDistance)}


# Calcul le chemin le plus rapide entre deux villes
def shortestRoute(start, end):
    global count
    count = 0

    villeDepart = Villes.getVilleByName(start)
    villeArriver = Villes.getVilleByName(end)
    global minWeight, path
    minWeight = None
    path = []

    def explore(villeName, weight, parents=[]):
        global count, minWeight, path
        count += 1

        ville = Villes.getVilleByName(villeName)
        voisins = sortByLowest(ville.voisins, villeArriver)

        if ville.nom in closedList:
            return
        closedList.append(ville.nom)
        parents.append(ville.nom)


        for k, v in voisins.items():

            if minWeight is not None and minWeight < (weight + v):
                continue

            if k == villeDepart.nom:
                continue

            if k == end:
                minWeight = weight + v
                path = parents.copy()


            elif k is not end and k not in parents:
                explore(k, weight + v, parents.copy())

    voisins = sortByLowest(villeDepart.voisins, villeArriver)
    for k, v in voisins.items():
        closedList = []
        if k == end:
            return
        else:
            explore(k, v, [])

    return {'paths': [start, *path, end], 'minWeight': minWeight}


# villeDepart = input('Entrer le nom de la ville d\'épart: ')
# villeArriver = input('Entrer le nom de la ville d\'arrivé: ')

start = time.time()
# shortestRoute(villeDepart, villeArriver)
end = time.time()
print('Temps écoulé: ', end - start)
