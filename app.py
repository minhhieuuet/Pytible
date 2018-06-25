from flask import Flask,request
from flask_pymongo import PyMongo
import os
import Chatible 
import time
from flask import json

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

@app.route('/getImage',methods=["GET"])
def getImage():
    return json.dumps({
  "messages": [
    {
      "attachment": {
        "type": "image",
        "payload": {
          "url": request.args.get('url')
        }
      }
    }
  ]
})

@app.route('/getVoice',methods=["GET"])
def getVoice():
  return json.dumps({
  "messages": [
    {
      "attachment": {
        "type": "audio",
        "payload": {
          "url": request.args.get('url')
        }
      }
    }
  ]
})

@app.route('/setFavorite',methods=["GET"])
def setFavorite():
  Chatible.setFavorite(request.args.get("senderId"),request.args.get("favorite"))
  return "1"

