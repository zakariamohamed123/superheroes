#!/usr/bin/env python3
#basic api managing super heroes and powers
from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
import os


from models import db, Hero, Power, HeroPower

app = Flask(__name__)
# Define the path to the database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


#database initializations
migrate = Migrate(app, db)
# initializes flask migrate extension with flask application
db.init_app(app)
#with sql alchemy database instance
# Routes

@app.route('/')
#defines a route for the homepage returning json indicating superheroes rule
def home():
    return jsonify({'message':'superheroes rule'})



@app.route('/heroes', methods=['GET'])
def get_heroes():
 #to retrieve all heroes from database  
    heroes = Hero.query.all()
    return jsonify([{'id': hero.id, 'name': hero.name, 'super_name': hero.super_name} for hero in heroes])

@app.route('/heroes/<int:hero_id>', methods=['GET'])
#a specific hero by id 
def get_hero(hero_id):
    hero = Hero.query.filter(Hero.id == hero_id).first()

    if hero:
        hero_dict = {
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name,
            'powers': [{'id': hero_power.power.id, 'name': hero_power.power.name, 'description': hero_power.power.description} for hero_power in hero.hero_power]
        }
        response = make_response(
            jsonify(hero_dict),
            200,
        )

        return response
    else:
        return jsonify({'error': 'Hero not found'}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{'id': power.id, 'name': power.name, 'description': power.description} for power in powers])

@app.route('/powers/<int:power_id>', methods=['GET', 'PATCH'])
#a specific power by id
def get_or_update_power(power_id):
    power = Power.query.get(power_id)

    if not power:
        return jsonify({'error': 'Power not found'}), 404

    if request.method == 'GET':
        return jsonify({'id': power.id, 'name': power.name, 'description': power.description})
    elif request.method == 'PATCH':
        #updates
        data = request.get_json()
        if 'description' in data:
            power.description = data['description']

            try:
                db.session.commit()
                return jsonify({'id': power.id, 'name': power.name, 'description': power.description})
            except:
                db.session.rollback()
                return jsonify({'errors': ['Validation errors']}), 400

if __name__ == '__main__':
#ensures flask devt starts if scripts is executed directly
    app.run(debug=True ,port=5555)
#export FLASK_RUN_PORT=5555