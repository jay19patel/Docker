from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['testdb']
collection = db['testcollection']


@app.route('/')
def index():
    data = collection.find()
    return render_template('index.html', collection=data)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        collection.insert_one({'name': name, 'email': email})
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    data = collection.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        collection.update_one({'_id': ObjectId(id)}, {'$set': {'name': name, 'email': email}})
        return redirect(url_for('index'))
    return render_template('edit.html', data=data)

@app.route('/delete/<id>')
def delete(id):
    collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))



