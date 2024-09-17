from flask import Flask
from pymongo import MongoClient
from .routes.registration_routes import registration_bp
from config import Config
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    CORS(app)

    app.mongo_client = MongoClient(app.config['MONGO_URI'])  
    app.db = app.mongo_client['demo_registrationDB']  

    app.register_blueprint(registration_bp)

    return app
