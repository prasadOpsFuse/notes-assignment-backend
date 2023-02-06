from configparser import ConfigParser 
  
configur = ConfigParser() 
configur.read('config.ini')

class Config:
    API_TITLE = "My API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = configur.get('dev','database_uri')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(
    dev = DevelopmentConfig
)
