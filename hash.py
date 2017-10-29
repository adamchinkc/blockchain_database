# MIT License
# Copyright (c) 2017 Adam K.C. Chin
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
