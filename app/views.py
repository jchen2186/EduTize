from flask import render_template
from app import app

@app.route('/')

@app.route('/index')
def index():
	return render_template("/index.html")

@app.route('/add_course')
def addCourse():
	return render_template("/add_course.html")

@app.route('/add_upcoming_assignment')
def addUpcoming():
	return render_template("/add_upcoming_assignment.html")