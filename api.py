import main
from flask import Flask, jsonify
from flask_cors import CORS
from Villes import Villes


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


@app.route('/api/villes/')
def getVilleByName(name):
    return jsonify({'villes': Villes.villes})

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True, host="0.0.0.0")
