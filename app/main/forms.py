from flask_wtf import FlaskForm
from wtforms import SubmitField

class PokemonForm(FlaskForm):
    submit = SubmitField('New Pokemon')