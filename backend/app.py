from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS


app= Flask(__name__)
api = Api(app)
CORS(app)

## This is what we're doing in MAD1 
# @app.route('/')
# def home():
#     return "Hello World!"

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}
    
api.add_resource(HelloWorld, '/message')

if __name__ == '__main__':
    app.run(debug=True)