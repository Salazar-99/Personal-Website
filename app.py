from flask import Flask, render_template, send_file
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from forms import PokemonForm
import os
import requests

#Define configs
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

#Load environment variables
load_dotenv()
config_name = os.getenv('CONFIG_NAME') or 'default'

#Create app
app = Flask(__name__)

#Set config
app.config.from_object(config[config_name])
config[config_name].init_app(app)
POKEMON_URL = os.getenv('POKEMON_URL')

#Initialize extensions
bootstrap = Bootstrap(app)

#Routes
@app.route('/')
def index():
    return render_template('index.html')

#TODO: Update POKEMON_URL once API is deployed
@app.route('/pokemon')
def pokemon():
    form = PokemonForm()
    if form.validate_on_submit():
        image = requests.get(POKEMON_URL)
        render_template('pokemon.html', image=image)
    render_template('pokemon.html', image=None)

#Entrypoint for Gunicorn
if __name__ == "__main__":
    app.run(host='0.0.0.0')
