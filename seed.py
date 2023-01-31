"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Make a bunch of Pets
p1 = Pet(name = 'Timmy',
species = 'Husky',
photo_url = 'https://images.pexels.com/photos/69433/pexels-photo-69433.jpeg',
age= 1,
notes= "Energetic and playful",
available= True)

p2 = Pet(name= 'Fluffy',
species= 'Cat',
photo_url= 'https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
age= 1.3,
notes= 'Calm and Loving')

p3 = Pet(name= 'Cookie',
species= 'Bunny',
photo_url= 'https://images.pexels.com/photos/96442/pexels-photo-96442.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
age= 0.5,
notes= 'Fun and loves carrot')

db.session.add_all([p1, p2, p3])

db.session.commit()