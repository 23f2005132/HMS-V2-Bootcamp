from flask_restful import Api, Resource

api = Api()

# This is what we NEED to do in mad2 (i.e, returning data instead of HTML)
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}
    
api.add_resource(HelloWorld, '/')

class PizzaAPI(Resource):
    def get(self):
        return {'pizza': 'Pizzas fetched succesfully!'}, 200
    
    def post(self):
        return {'message': 'Pizza created!'}, 201
    
    def put(self):
        return {'message': 'Pizza updated!'}, 200
    
    def delete(self):
        return {'message': 'Pizza deleted!'}, 200
    
api.add_resource(Pizza, '/pizza')