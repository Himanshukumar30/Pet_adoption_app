from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import URL, Optional, InputRequired, Length, NumberRange

class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators = [InputRequired('Name cant be empty')])
    species = SelectField('Species', choices = [('cat', 'Cat'), ("dog", "Dog"), ('bunny', 'Bunny')])
    photo = StringField('Photo URL', validators = [Optional(), URL()])
    age = IntegerField('Age', validators = [NumberRange(min=0, max=30)])
    notes = StringField('Notes')
    available = BooleanField('available?')

class EditPetForm(FlaskForm):

    name = StringField('Pet Name', validators = [InputRequired('Name cant be empty')])
    species = SelectField('Species', choices = [('cat', 'Cat'), ("dog", "Dog"), ('bunny', 'Bunny')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")