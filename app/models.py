#
from flask_sqlalchemy import SQLAlchemy
#mports the SQLAlchemy extension that provide tools in flaks applications
db = SQLAlchemy()
#it creates an instance of sqlalchemy that is used to interact with database
class Hero(db.Model):
    # the hero inherits from db model
    #db model base class defining database models
    __tablename__ = 'heroes'
#specifies the name of the database table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    super_name = db.Column(db.String(50), nullable=False)

    # Relationship with HeroPower
    hero_power = db.relationship('HeroPower', backref='hero')

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    # Relationship with Hero through HeroPower
    power_heroes = db.relationship('HeroPower', backref='power')

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)
    strength = db.Column(db.String(20), nullable=False)

   
