from flask import Flask, render_template
from config import config, config_name
import os

#Create app
app = Flask(__name__)

#Set config
app.config.from_object(config[config_name])
config[config_name].init_app(app)

#Home page
@app.route('/')
def index():
    return render_template('index.html')