import json
import main
from flask import Flask, jsonify
from flask_cors import CORS
from Villes import Villes
import requests

global villes

hereApi = 'jwdvUmFcg-KUIdCUxcs7doiBx03uipAbTsgvfr-VNT0'
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/<name>/')
def getVilleByName(name):
    ville = Villes.getVilleByName(name)
    if ville:
        return jsonify({
            'name': ville.nom,
            'latitude': ville.lat,
            'longitude': ville.long,
            'voisins': ville.voisins
        }), 200
    return jsonify({'error': 'Ville introuvable'})


@app.route('/api/<ville1>/<ville2>/')
def routeBetween(ville1, ville2):
    if Villes.villeExist(ville1) and Villes.villeExist(ville2):
        route = main.shortestRoute(ville1, ville2)
        if route:
            return jsonify(route)
        return jsonify({'error': 'Route introuvable'})
    return jsonify({'error': 'Une des villes n\'existe pas'})


@app.route('/api/exist/<ville>')
def exist(ville):
    return jsonify({'status': Villes.villeExist(ville)})


def getGeocode(address):
    url = "https://geocoder.ls.hereapi.com/search/6.2/geocode.json?languages=fr-FR&maxresults=1&searchtext=" + address + "&apiKey=" + hereApi
    response = requests.get(url)
    json = response.json()
    return json['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']


def loadGeocodes():
    global villes
    with open('./geocodes.json', 'r') as file:
        villes = json.load(file)

@app.route('/api/villes/')
def getVilles():
    global villes
    return jsonify({'villes': villes})


loadGeocodes()
if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True, host="0.0.0.0")
