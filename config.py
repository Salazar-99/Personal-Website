import os
from dotenv import load_dotenv

#Load environment variables
load_dotenv()
config_name = os.getenv('CONFIG_NAME') or 'default'

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    #Boilerplate for Flask configs
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}