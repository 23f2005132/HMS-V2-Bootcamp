from flask import Flask
from flask_cors import CORS

app= Flask(__name__)
CORS(app)

# connecting to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
from models import db
db.init_app(app)

# connecting routes
from routes import api  # Ensure routes are imported to register them with the app
api.init_app(app)

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()  # Create database tables for our data models

    app.run(debug=True)