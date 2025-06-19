from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to HBnB API!"})

    return app

from flask_restx import Namespace, Resource, fields
from hbnb.services.facade import HBnBFacade  

user_ns = Namespace('users', description='User operations')
facade = HBnBFacade()

user_model = user_ns.model('User', {
    'id': fields.String(readonly=True, description='User ID'),
    'email': fields.String(required=True, description='User email'),
    'first_name': fields.String(description='First name'),
    'last_name': fields.String(description='Last name'),
})
