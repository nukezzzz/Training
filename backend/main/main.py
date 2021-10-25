from flask import Flask
from bson.json_util import dumps
from bson import json_util
from flask_pymongo import PyMongo
from flask import jsonify, make_response
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# app.config[
#     'MONGO_URI'] = "mongodb://mongo-service:27017/cricket"
app.config[
    'MONGO_URI'] = "mongodb://localhost:27017/cricket"
mongo = PyMongo(app)


@app.route('/listall')
def listAllData():
    matches = mongo.db.matches.find()
    resp = dumps(matches)
    return resp


@app.route('/countrylist')
def countrylist():
    matches = mongo.db.matches.distinct("Country")
    resp = dumps(matches)
    return resp


@app.route('/srilankahistory')
def lankaHistory():
    matches = list(mongo.db.matches.find({'Country': "Sri Lanka"}))
    return json.dumps(matches, default=json_util.default)
    # res = make_response(jsonify(matches), 200)
    # return res


@app.route('/view/<country>')
def country(country):
    matches = list(mongo.db.matches.find({'Country': country}))
    return json.dumps(matches, default=json_util.default)
    # res = make_response(jsonify(matches), 200)
    # return res

@app.route('/stats/<country>')
def filterCountryStats(country):
    won = 0
    canceled = 0
    tied = 0
    lost = 0
    filtered = mongo.db.matches.find({'Country': country})
    if filtered.count() == 0:
        return make_response(jsonify({"count": "No data Found"}), 200)
    else:
        print("Entry Found")
    for match in filtered:
        # print(match, file=sys.stdout)
        if match['Result'] == 'Won':
            won += 1
        elif match['Result'] == 'Lost':
            lost += 1
        elif match['Result'] == 'Tied':
            tied += 1
        else:
            canceled += 1
    # print(f'Country :{country}', file=sys.stdout)
    # print(f'Won :{won} , Lost :{lost} , Tied : {tied} ,  Canceled :{canceled} , Count : {filtered.count()}',
    #       file=sys.stdout)
    response = [{
        "Country": country,
        "Won": won,
        "Lost": lost,
        "Tied": tied,
        "Count": filtered.count(),
        "Canceled": canceled
    }]
    res = make_response(jsonify(response), 200)
    return res


@app.route('/')
def hello():
    return "Hello This is ROOT DOC"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
    # from waitress import serve

    # serve(app, host="0.0.0.0", port=5000)
