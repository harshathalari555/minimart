from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient

app = Flask(__name__)

# Configure SQLAlchemy connection
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/postgres'
# db = SQLAlchemy(app)

# Configure MongoDB connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/local'
mongo = MongoClient(app.config['MONGO_URI'])
db = SQLAlchemy(app)




# Define SQLAlchemy model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.Text)
    image_url = db.Column(db.Text)

    def __repr__(self):
        return '<Product %r>' % self.product_name

class User(db.Document):
    username = mongo.db.StringField(unique=True, required=True)
    email = mongo.db.StringField(unique=True, required=True)
    password = mongo.db.StringField(required=True)


# Access a specific MongoDB database
mongo_db = mongo.get_database()

# Now you can interact with the MongoDB database within Flask routes
@app.route('/')
def index():
    # Example: Inserting a document into a collection
    mongo_db.mycollection.insert_one({'key': 'value'})
    return 'Document inserted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
