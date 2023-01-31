from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import URL, Optional, InputRequired, Length, AnyOf

class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators = [InputRequired('Name cant be empty')])
    species = StringField('Species', validators = [AnyOf('cat', 'dog', 'bunny')])
    photo = StringField('Photo URL', validators = [Optional(), URL()])
    age = FloatField('Age', validators = [Length(min=0, max=30)])
    Notes = StringField('Notes')

class EditPetForm(FlaskForm):

    name = StringField('Pet Name', validators = [InputRequired('Name cant be empty')])
    species = StringField('Species', validators = [AnyOf('cat', 'dog', 'bunny')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")