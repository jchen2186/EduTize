from flask import render_template, request
from app import app
import sys
import os

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

@app.route('/completed-task',methods = ['GET','POST'])
def addCompletedTask():
	if request.method == 'POST':
		name = request.form['taskName']
		course = request.form['course']
		category = request.form['category']
		grade = request.form['grade']
		# task = Assignment(course,category,name)
		pathName = "data/user001/" + course
		if ((os.path.isdir(pathName)) == False): # if directory does not exist
			os.mkdir(pathName) # create the directory
		pathName += "/" + name + ".txt"
		fo = open(pathName,'w')
		fo.write(name + "\n")
		fo.write(course + "\n")
		fo.write(category + "\n")
		fo.close()
		return "Task is added!"
	else:
		return render_template("/completed_task.html")