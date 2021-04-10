import time

class Ville:
    def __init__(self, nom, lat, long):
        self.nom = nom
        self.lat = int(lat)
        self.long = int(long)
        self.voisins = {}




def analyser(lignes,index):
    voisins = {}
    nbrlignes = len(lignes)

    for i in range (index+1,nbrlignes):


        ligne = lignes[i]


        if len(ligne.split()) == 2 :
            (villeV,distance) = ligne.split()
            voisins[villeV] = int(distance)

        elif len(ligne.split()) == 3 :
            return voisins

    return voisins


def charger(dicVilles,file):
    file = open(file,"r")
    lignes = file.readlines()
    file.close()

    for i in range (0,len(lignes)):
        l = lignes[i]
        if len(l.split()) == 3:
            (nom, lat, long) = l.split()
            ville = Ville(nom, lat, long)
            dicVilles.update({ville.nom: ville})
            voisins = analyser(lignes,i)
            ville.voisins = voisins






dictionnaireVilles = {}
charger(dictionnaireVilles,"FRANCE.MAP")
print(dictionnaireVilles)
print(dictionnaireVilles["Calais"].voisins)


a = "Rennes"
b = "Moulins"
villeDepart = a
villeArriver = b



def distanceBeetwen (loc1, loc2):
    result = abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1])
    return result / 4


def getVilleByName(villeName):
    return dictionnaireVilles[villeName]

def sortByLowest(voisins, ville):
    dict = {}
    for k , v in voisins.items() :
        voisin = getVilleByName(k)
        distance = distanceBeetwen([ville.lat, ville.long], [voisin.lat, voisin.long])
        dict[voisin.nom] = distance

    return {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}


def shortestRoute(start, end):
    global count
    count = 0

    global weight
    weight = 0
    villeDepart = getVilleByName(start)
    villeArriver = getVilleByName(end)
    global minWeight
    minWeight = None


    def explore(villeName, weight, parent=None):
        global count
        global minWeight
        count += 1
        ville = getVilleByName(villeName)
        voisins = sortByLowest(ville.voisins, villeArriver)

        if ville.nom in closedList:
            return
        closedList.append(ville.nom)


        for k, v in voisins.items():

            if k == end:
                print(parent)
                print(ville.nom)
                print(closedList)
                print("----------------------------------")
                minWeight = weight

                return

            elif parent != k:
                if minWeight == None or minWeight > (weight + v):
                    explore(k, weight + v, ville.nom)

    voisins = sortByLowest(villeDepart.voisins, villeArriver)
    print(voisins)
    for k, v in voisins.items():
        closedList = []
        if k == end:
            return
        else:
            print(k)
            explore(k, v, villeDepart.nom)


    print(count)


start = time.time()
shortestRoute(villeDepart, villeArriver)
end = time.time()
print(end - start)
# plusProche = Closest(villeDepart)
# print(plusProche)