from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/add_course')
@app.route('/add_upcoming_assignment')

def index():
	return render_template("/index.html")

def addCourse():
	return render_template("/add_course.html")

def addUpcoming():
	return render_template("/add_upcoming_assignment.html")