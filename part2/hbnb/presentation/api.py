from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to HBnB API!"})

    return app
