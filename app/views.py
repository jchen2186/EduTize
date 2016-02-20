from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'}  # fake user
	# add buttons to add course, assignments or whatever
	return render_template("index.html",
						   title='Home',
						   user=user)