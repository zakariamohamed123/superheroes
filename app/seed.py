#!/usr/bin/env python3

from app import app, db
from models import Hero, Power, HeroPower
import random 
from sqlalchemy import func 

with app.app_context():
    # Delete existing data
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    # Powers
    powers_data = [
        {"name": "Detective Skills", "description": "Master detective skills"},
        {"name": "Super Strength", "description": "Incredibly strong"},
        {"name": "Telekinesis", "description": "Move objects with the mind"},
        {"name": "Invisibility", "description": "Become invisible at will"}
    ]

    for power_info in powers_data:
        power = Power(**power_info)
        db.session.add(power)

    # Heroes
    heroes_data = [
        {"name": "Batman", "super_name": "Bruce Wayne"},
        {"name": "Superman", "super_name": "Clark Kent"},
        {"name": "Wonder Woman", "super_name": "Diana Prince"},
        {"name": "The Flash", "super_name": "Barry Allen"},
        {"name": "Green Lantern", "super_name": "Hal Jordan"},
        {"name": "Aquaman", "super_name": "Arthur Curry"},
        {"name": "Black Canary", "super_name": "Dinah Lance"},
        {"name": "Green Arrow", "super_name": "Oliver Queen"},
        {"name": "Martian Manhunter", "super_name": "J'onn J'onzz"},
        {"name": "Hawkgirl", "super_name": "Shayera Hol"}
    ]

    for hero_info in heroes_data:
        hero = Hero(**hero_info)
        db.session.add(hero)

    
    db.session.commit()

    # Adding Powers to Heroes
    strengths = ["High", "Medium", "Low"]

    for hero in Hero.query.all():
        for _ in range(random.randint(1, 3)):
            power = Power.query.order_by(func.random()).first()  # Randomly select a power
            hero_power = HeroPower(hero_id=hero.id, power_id=power.id, strength=random.choice(strengths))
            db.session.add(hero_power)

   
    db.session.commit()
