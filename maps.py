import main
import matplotlib.pyplot as plt

dictionnaireVilles = {}
main.charger(dictionnaireVilles, "FRANCE.MAP")
print(dictionnaireVilles)

coords = []
labels = []
for k, v in dictionnaireVilles.items():
    coords.append([v.lat, v.long])
    labels.append(k)

x, y = zip(*coords)
plt.scatter(x, y)
for i in range(0, len(coords)):
    plt.annotate(labels[i], (coords[i][0], coords[i][1] + 25))
plt.show()