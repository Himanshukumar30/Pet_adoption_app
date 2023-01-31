from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "vancouverisawesome123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    '''Homepage'''
    
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)

@app.route('/add', methods =['GET', 'POST'])
def add_pet():
    '''Handle add new pet form GET and POST'''
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        new_pet = Pet(name=name, species=species ,photo_url= photo, age=age ,notes=notes, available = available)
        
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Added {name},I am a {species} and my age is {age}")
        return redirect('/')
    else:
        return render_template("add_pet.html", form=form)
    
@app.route('/<pet_id>', methods= ['GET', 'POST'])
def show_pet_info(pet_id):
    '''Show pet information and handle edit form'''
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        # db.session.update(pet)
        db.session.commit()
        flash(f"Updated {pet.name},I am a {pet.species} and my age is {pet.age}")
        return redirect('/')
    else:
        return render_template('edit_pet_info.html', pet=pet,form=form)