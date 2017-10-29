# MIT License
# Copyright (c) 2017 Adam K.C. Chin
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sqlite3
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps, loads
from flask_jsonpify import jsonpify
import json
import requests


def call_hash(data):
	url = 'http://127.0.0.1:8002/hash/'
	try:
		del data['hash']
	except:
		pass
	data2={}
	data2['data']=json.dumps(data)
	#print data2
	response = requests.post(url, data=data2, allow_redirects=False)
	if  response.status_code == 200:
		return response.json()['hash']

def call_nouce():
	nouce_url = 'http://127.0.0.1:8001/nouce'
	response = requests.get(nouce_url)
	if  response.status_code == 200:
		return response.json()['nouce']


def get_pre_hash(cursor):
	cursor.execute('select * from journal order by id desc limit 1')
	results = cursor.fetchall()
	if results:
		return results[0]['hash']
	else:
		return ""


def database_connect():
	conn = sqlite3.connect('blockchain.db')
	conn.row_factory = dict_factory
	cursor = conn.cursor()
	return conn, cursor


def data_contruct_new(data1):
	nouce = {"nouce":u""}
	hash = {"hash":u""}
	pre_hash =  {"pre_hash":u""}
	data1.update(nouce)
	data1.update(hash)
	data1.update(pre_hash)
	return data1

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

app = Flask(__name__)




@app.route("/insert", methods = ['GET', 'POST'])
def insert():
  	if request.method == 'POST':
  		data = request.form['data']
   		data1 = loads(data)
   		conn, cursor = database_connect()
   		try:
   			cursor.execute("insert into journal(journal_id, entry_date, create_time, created_by, post_status, account_code, amount, dr_cr, nouce, hash) values ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [ data1['journal_id'], data1['entry_date'], data1['create_time'], data1['created_by'], data1['post_status'], data1['account_code'], data1['amount'], data1['dr_cr'], data1['nouce'], data1['hash']])
   			conn.commit()
   			return "Success"
   		except:
   			return "Failed"
   		conn.close()
   	else:
   		return ""


@app.route("/verify", methods = ['GET', 'POST'])
def verify():
	if request.method == 'GET':
  		try:
	  		id = request.args.get('id', default = 2, type = int)
	   		conn, cursor = database_connect()
			cursor.execute('select * from journal where id <= ? order by id desc limit 2', [id,])
			results = cursor.fetchall()
			records_verify = results[0]
			hash_now = results[0]['hash']
			pre_hash =  {u"pre_hash":u""}
			records_verify.update(pre_hash)
			records_verify['pre_hash'] = results[1]['hash']
			del records_verify['id']
			hash_value = call_hash(records_verify)
			conn.close()
			if hash_value == hash_now:
				return "Verified"
			else:
				return "Failed"
   		except:
   			return "Error"
   		conn.close()
   	else:
   		return ""


@app.route("/construct", methods = ['GET', 'POST'])
def construct():
	if request.method == 'POST':
		data = request.form['data']
		data1 = loads(data)
		conn, cursor = database_connect()
		data1 = data_contruct_new(data1)
		data1['pre_hash'] = get_pre_hash(cursor)
		data1['nouce'] = call_nouce()
		data1['hash'] = call_hash(data1)
		conn.close()
		return jsonpify(data1)
   	else:
   		return ""


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8000')
