from flask import Flask
from flask_restx import Api
from app.api.user import api as user_ns  # On importera d'autres namespaces ici plus tard

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API',
              description='API for the HBnB Application')

    # Enregistrement des namespaces (routes)
    api.add_namespace(user_ns, path='/users')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
