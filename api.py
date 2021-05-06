import json

from flask import Flask, jsonify, make_response, request
from flask_restplus import Resource, Api, fields
from flask_bcrypt import generate_password_hash, check_password_hash, Bcrypt
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_cors import CORS
from json2xml import json2xml

import main
from Villes import Villes
from Auth import Auth

app = Flask(__name__)
api = Api(app, title='ProjetLPI - Astar', description='Un projet scolaire pour comprendre l\'algo Astar', default='Astar API' )
bcrypt = Bcrypt(app)
app.config['JWT_SECRET_KEY'] = 'A@6?NAcYLa?!Y#os5aSCxXHB49r'
jwt = JWTManager(app)


app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False
CORS(app, resources={r"/*": {"origins": "*"}})

users = {
    "admin": generate_password_hash("admin").decode('utf8')
}


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

    def post(self):
        return

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


@api.route('/admin/login')
@api.doc(description="Connecte un utilisateur en stockant un jeton jwt dans les cookies")
class Login(Resource):
    resource_fields = api.model('Login', {
        'username': fields.String,
        'password': fields.String,
    })

    @api.expect(resource_fields)
    def post(self):
        return Auth.login()

@api.route('/admin/logout')
@api.doc(description="Déconnecte un utilisateur en supprimant le jeton de ces cookies")
class Logout(Resource):
    @jwt_required()
    def get(self):
        return Auth.logout()


@api.route('/admin')
class Admin(Resource):
    @jwt_required()
    def get(self):
        arr = [ob.__dict__ for ob in Villes.villes.values()]
        return jsonify({'villes': arr})


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
