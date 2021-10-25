from flask import Flask
from bson.json_util import dumps
from flask_pymongo import PyMongo
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MONGO_URI'] = os.environ['MONGODB_URI']
# os.environ['MONGODB_URI']  mongodb://mongo-service:27017/cricket
mongo = PyMongo(app)


@app.route('/listall')
def listAllData():
    matches = mongo.db.matches.find()
    resp = dumps(matches)
    return resp


@app.route('/')
def hello():
    return "Hello This is ROOT DOC"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
