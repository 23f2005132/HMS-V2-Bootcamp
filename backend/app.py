from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = "super-secret"
jwt = JWTManager(app)

CORS(app)

# cache configuration
from routes import cache
app.config['CACHE_TYPE'] = 'RedisCache'
app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'
cache.init_app(app)

# connecting to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
from models import db, User
db.init_app(app)

# connecting to routes
from routes import api
api.init_app(app)

if __name__ == '__main__':
        
    with app.app_context():

        db.create_all()  # Create database tables for our data models

        admin = User.query.filter_by(email='admin@gmail.com').first()

        if not admin:
            admin = User(email='admin@gmail.com', password='admin', role='admin', name='Admin User')
            db.session.add(admin); db.session.commit()
            print("Admin user created with email: admin@gmail.com and password: admin")
        else:
            print("Admin user already exists with email: admin@gmail.com and password: admin")
        
    app.run(debug=True)