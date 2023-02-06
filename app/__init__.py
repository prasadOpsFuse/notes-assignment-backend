from flask import Flask
from flask_smorest import Api
from app.config import config_by_name
from app.db import db
from app.main.controllers.folder_controller import folder_blueprint
from app.main.controllers.notes_controller import notes_blueprint
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_by_name['dev'])
    db.init_app(app)
    api = Api(app)
    with app.app_context():
        db.create_all()
    
    api.register_blueprint(folder_blueprint)
    api.register_blueprint(notes_blueprint)
    return app