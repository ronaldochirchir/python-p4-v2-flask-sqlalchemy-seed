#!/usr/bin/env python3
# server/seed.py

from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

# Creating an application context
with app.app_context():

    # Initialize Faker instance
    fake = Faker()

    # Clear existing data
    Pet.query.delete()

    # List of possible species
    species_list = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Create new pet records
    pets = [Pet(name=fake.first_name(), species=rc(species_list)) for _ in range(10)]

    # Add to the session and commit
    db.session.add_all(pets)
    db.session.commit()

    print("Database successfully seeded with random pets!")
