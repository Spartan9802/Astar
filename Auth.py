from flask import make_response, request, redirect, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash, Bcrypt
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies
import datetime

users = {
    "admin": generate_password_hash("admin").decode('utf8')
}


class Auth:

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password).decode('utf8')

    @staticmethod
    def check_password(password, hash):
        return check_password_hash(hash, password)

    @staticmethod
    def login():
        body = request.get_json()
        if not body.get('username') in users:
            return {'error': 'Nom ou mot de passe incorrect'}, 401

        user = users.get(body.get('username'))
        authorized = Auth.check_password(body.get('password'), user)
        if not authorized:
            return {'error': 'Nom ou mot de passe incorrect'}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(body.get('username')), expires_delta=expires)
        return jsonify({'jwt': access_token})

    @staticmethod
    def logout():
        resp = make_response(jsonify({'success': 'Vous avez été déconnecté avec succès'}))
        unset_jwt_cookies(resp)
        return resp
