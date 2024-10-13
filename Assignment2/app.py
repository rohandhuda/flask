from flask import Flask
from pymongo import MongoClient
from flask import render_template

app = Flask(__name__)


# MongoDB connection setup
client = MongoClient("mongodb+srv://root:SGo0uffpFHQ2euzO@cluster0.5cx8t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.shop_db
products_collection = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = products_collection.find()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run()