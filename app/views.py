from flask import render_template
from app import app

@app.route('/')

@app.route('/index')
def index():
	return render_template("/index.html")

@app.route('/new-course')
def addNewCourse():
	return render_template("/new_course.html")

@app.route('/completed-course')
def addCompletedCourse():
	return render_template("/completed_course.html")

@app.route('/new-task')
def addNewTask():
	return render_template("/new_task.html")

@app.route('/completed-task')
def addCompletedTask():
	return render_template("/completed_task.html")