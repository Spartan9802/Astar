from flask import Flask, jsonify, make_response
from flask_restplus import Resource, Api
from json2xml import json2xml

import main
from Villes import Villes

app = Flask(__name__)
api = Api(app, title='ProjetLPI - Astar', description='Un projet scolaire pour comprendre l\'algo Astar', default='Astar API' )

app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False


@api.representation('application/xml')
def xml(data, code, headers):
    resp = make_response(json2xml.Json2xml(data).to_xml(), code)
    resp.headers.extend(headers)
    return resp


@api.route('/villes/')
@api.doc(description="Retourne la liste des villes avec le geocodage réel")
class Ville(Resource):

    def get(self):
        return main.villes

@api.route('/villes/<string:ville>')
@api.doc(params={'ville': 'Est une ville'}, description="Retourne les informations d'une ville")
class Ville(Resource):

    def get(self, ville):
        ville_obj = Villes.getVilleByName(ville)
        if ville_obj:
            return ville_obj.__dict__
        return jsonify({'error': 'Ville introuvable'})

@api.route('/trajet/<string:start>/<string:end>')
@api.doc(params={'start': 'Est la ville de départ', 'end': 'Est la ville d\'arrivé'}, description="Retourne le trajet le plus court entre deux villes")
class Trajet(Resource):

    def get(self, start, end):
        if Villes.villeExist(start) and Villes.villeExist(end):
            route = main.shortestRoute(start, end)
            if route:
                return route
            return jsonify({'error': 'Route introuvable'})
        return jsonify({'error': 'Une des villes n\'existe pas'})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
