#hash

from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps, loads
from flask_jsonpify import jsonpify

from hashlib import sha256

app = Flask(__name__)


@app.route("/hash/", methods = ['GET', 'POST'])
def hash():
  	if request.method == 'POST':
  		data = request.form['data']
   		data_sha256 = sha256(dumps(loads(data), sort_keys=True).encode('utf-8')).hexdigest()
   		hashjson = {'hash': data_sha256}
   		return jsonpify(hashjson)
   	else:
   		return ' '

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8002')
