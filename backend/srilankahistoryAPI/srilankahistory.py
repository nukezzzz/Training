from flask import Flask
from bson import json_util
from flask_pymongo import PyMongo
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MONGO_URI'] = os.environ['MONGODB_URI']
# os.environ['MONGODB_URI']  mongodb://mongo-service:27017/cricket
mongo = PyMongo(app)


@app.route('/srilankahistory')
def lankaHistory():
    matches = list(mongo.db.matches.find({'Country': "Sri Lanka"}))
    return json.dumps(matches, default=json_util.default)


@app.route('/')
def hello():
    return "Hello This is ROOT DOC"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
