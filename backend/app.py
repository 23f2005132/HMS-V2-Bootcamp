from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app= Flask(__name__)

app.config['JWT_SECRET_KEY'] = "super-secret"
jwt = JWTManager(app)

CORS(app)

# connecting to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
from models import db, User
db.init_app(app)

# connecting routes
from routes import api  # Ensure routes are imported to register them with the app
api.init_app(app)

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()  # Create database tables for our data models

        admin = User.query.filter_by(email='admin@gmail.com').first()

        if not admin:
            admin = User(email='admin@gmail.com', password='adminpass', role='admin')
            db.session.add(admin)
            db.session.commit()
            print("Admin user created. Email: admin@gmail.com and password: adminpass")
        else:
            print("Admin user already exists.")

    app.run(debug=True)