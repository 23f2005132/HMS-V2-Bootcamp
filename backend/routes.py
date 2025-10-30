from flask_restful import Api, Resource
from flask import request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from models import db, User, Pizza

api = Api()

## Test Endpoints


# This is what we NEED to do in mad2 (i.e, returning data instead of HTML)
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}
    
api.add_resource(HelloWorld, '/')

## AUTH endpoints

class Registration(Resource):
    def post(self):
        data = request.get_json()
        # Registration logic here
        if not data or 'email' not in data or 'password' not in data:
            return {'message': 'Email and password are required!'}, 400

        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return {'message': 'User already exists!'}, 400

        new_user = User(email=data['email'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully!'}, 201
api.add_resource(Registration, '/register')

class Login(Resource):
    def post(self):
        data = request.get_json()
        if not data or 'email' not in data or 'password' not in data:
            return {'message': 'Email and password are required!'}, 400
        
        user = User.query.filter_by(email=data['email'], password=data['password']).first()
        if not user:
            return {'message': 'Invalid credentials!'}, 401
        
        token = create_access_token(identity=user.email)
        
        return {'message': 'Login successful!', 'token': token, 'user': {'email': user.email, 'role': user.role}}, 200
api.add_resource(Login, '/login')

## USER endpoints

class PizzaAPI(Resource):
    @jwt_required()
    def get(self, pizza_id=None):
        if pizza_id:
            pizza = Pizza.query.get(pizza_id)
            if not pizza:
                return {'message': 'Pizza not found'}, 404
            return {'pizza': {'id': pizza.id, 'name': pizza.name, 'price': pizza.price}}, 200
        pizzas=Pizza.query.all()
        # print(pizzas)
        pizzas = [{'id': p.id, 'name': p.name, 'toppings': p.toppings} for p in Pizza.query.all()]
        # print(pizzas)
        return {'pizza': 'Pizzas fetched succesfully!', "pizzas":pizzas}, 200
    
    @jwt_required()
    def post(self):
        user = User.query.filter_by(email=get_jwt_identity()).first()
        if user.role != 'admin':
            return {'message': 'Admin privilege required!'}, 403

        data = request.get_json()

        if not data or 'name' not in data and not data['name']:
            return {'message': 'Name is required!'}, 400
        
        pizza = Pizza(name=data['name'], toppings=data.get('toppings', False))
        db.session.add(pizza)
        db.session.commit()

        return {'message': 'Pizza created!'}, 201
    
    @jwt_required()
    def put(self, pizza_id=None):
        user = User.query.filter_by(email=get_jwt_identity()).first()
        if user.role != 'admin':
            return {'message': 'Admin privilege required!'}, 403

        if pizza_id is None:
            return {'message': 'Pizza ID is required for update!'}, 400
        
        # check pizza exists or not
        pizza = Pizza.query.get(pizza_id)
        if not pizza:
            return {'message': 'Pizza not found!'}, 404
        
        # get data and validate
        data = request.get_json()
        if not data:
            return {'message': 'Data is required!'}, 400
        
        pizza.name = data.get('name', pizza.name)
        pizza.toppings = data.get('toppings', pizza.toppings)
        db.session.commit()

        return {'message': 'Pizza updated!'}, 200

    @jwt_required() 
    def delete(self, pizza_id=None):
        user = User.query.filter_by(email=get_jwt_identity()).first()
        if user.role != 'admin':
            return {'message': 'Admin privilege required!'}, 403
        if pizza_id is None:
            return {'message': 'Pizza ID is required for deletion!'}, 400
        
        pizza = Pizza.query.get(pizza_id)
        if not pizza:
            return {'message': 'Pizza not found!'}, 404
        
        db.session.delete(pizza); db.session.commit()

        return {'message': 'Pizza deleted!'}, 200
    
api.add_resource(PizzaAPI, '/pizza', '/pizza/<int:pizza_id>')