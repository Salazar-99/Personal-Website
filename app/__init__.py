from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from .config import config
from dotenv import load_dotenv

load_dotenv(".env")

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app