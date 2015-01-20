from flask import Flask, render_template, request

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

import os
import requests
import sys
import json

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api_manager = APIManager(app, flask_sqlalchemy_db=db)

from models import *

# @app.route('/')
# def hello():
    # return "Hello World!"


# @app.route('/<name>')
# def hello_name(name):
    # return "Hello {}!".format(name)
	
# notice the different between request and requestS
@app.route('/', methods=['GET', 'POST'])
def index():
	errors = []
	results = []
	if request.method == 'POST':
		try:
			url = request.form['url']
			errors.append('url: ' + url);
			r = requests.get(url)
			errors.append('text: ' + r.text);
		except Exception,e:
			errors.append('Failed: ' + str(e));
	return render_template('index.html', errors=errors, results=results)
	
@app.route('/logmein', methods=['POST'])
def log_me_in():
	data = json.loads(request.data)	
	user = User('quan', 'pham', data['username'], data['password'])
	db.session.add(user)
	db.session.commit()
	return 'Welcome ' + data['username'];
	
	
if __name__ == '__main__':
    app.run()