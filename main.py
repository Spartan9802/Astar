from DataBase import FileLoader
from Villes import Villes

fileLoader = FileLoader("./FRANCE.MAP")
Villes.addVilles(fileLoader.parse())

# Récupére la distance entre deux positions
def distanceBetween(loc1, loc2):
    result = abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])
    return result / 4

def somme(arr):
    somme = 0
    for i in arr:
        somme += i
    return somme

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

    def explore(villeName, weight, parents={}):
        global count, minWeight, path
        count += 1

        ville = Villes.getVilleByName(villeName)
        voisins = sortByLowest(ville.voisins, villeArriver)

        parents[ville.nom] = weight

        for k, v in voisins.items():

            if minWeight is not None and minWeight < (somme(parents.values()) + v):
                continue

            if k in parents.keys():
                continue

            if k == villeDepart.nom:
                continue

            if k == villeArriver.nom:
                paths = parents.copy()
                paths[k] = v
                minWeight = somme(paths.values())
                path = paths


            elif k is not end and k not in parents:
                explore(k, v, parents.copy())

    voisins = sortByLowest(villeDepart.voisins, villeArriver)
    for k, v in voisins.items():
        if k == end:
            path = {villeDepart.nom: 0, k: v}
            minWeight = v
            break
        else:
            explore(k, v, {villeDepart.nom: 0})
    return {'paths': path, 'minWeight': minWeight}


