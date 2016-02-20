from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/add_course')
@app.route('/add_upcoming_assignment')

def index():
	user = {'nickname': 'Miguel'}  # fake user
	# add buttons to add course, assignments or whatever
	return render_template("index.html",
						   title = 'Home',
						   user = user)

def addCourse():
	return render_template("add_course.html",
							title = "Add Course",
							user = user)

def addUpcoming():
	return render_template("add_upcoming_assignment.html",
							title = "Add Upcoming Assignment",
							user = user)