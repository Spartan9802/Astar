#!/usr/bin/env python
# encoding: utf-8
import main
from flask import Flask, render_template, jsonify
from Villes import Villes

app = Flask(__name__)

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
    return jsonify({'error': 'Ville introuvable'}), 404


@app.route('/api/<ville1>/<ville2>/')
def routeBetween(ville1, ville2):
    route = main.shortestRoute(ville1, ville2)
    if route:
        return jsonify(route), 200
    return jsonify({'error': 'Route introuvable'}), 404


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True, host="0.0.0.0")
