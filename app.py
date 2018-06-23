from flask import Flask,request
from flask_pymongo import PyMongo
import os
import Chatible 
import time

app = Flask(__name__)
app.config['MONGO_URI']=os.getenv("MONGO_URI")
app.config['MONGO_DBNAME']=os.getenv("MONGO_DBNAME")
mongo = PyMongo(app)
@app.route('/',methods=["GET"])
def index():
    return "Its works!"

@app.route('/chatible', methods=['POST']) 
def chatible():
    Chatible.handleUser(request.form["senderId"],int(time.time()*10e4),request.form['msg'],request.form['name'],request.form['profile_pic'],request.form['gender'])
    return "1";