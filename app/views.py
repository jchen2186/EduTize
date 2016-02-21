from flask import render_template, request
from app import app
import sys
import os

@app.route('/')

@app.route('/index')
def index():
	return render_template("/index.html")

@app.route('/new-course', methods = ['GET', 'POST'])
def addNewCourse():
	if request.method == 'POST':
		course = request.form['course']
		gpa = request.form['GPA']
		pathName = "data/user001/" + course
		if ((os.path.isdir(pathName)) == False): # if directory does not exist
			os.mkdir(pathName) # create the directory
		pathName += "/" + course + ".txt"
		fo = open(pathName,'w')
		fo.write(course + "\n")
		fo.write("\n") # skipping line because this is for actual gpa
		fo.write(gpa + "\n") # this line is for goal gpa
		fo.close()
		return render_template("/new_course_confirmation.html")
	else:
		return render_template("/new_course.html")

@app.route('/completed-course', methods = ['GET', 'POST'])
def addCompletedCourse():
	if request.method == 'POST':
		course = request.form['course']
		gpa = request.form['GPA']
		pathName = "data/user001/" + course
		if ((os.path.isdir(pathName)) == False): # if directory does not exist
			os.mkdir(pathName) # create the directory
		pathName += "/" + course + ".txt"
		fo = open(pathName,'w')
		fo.write(course + "\n")
		fo.write(gpa + "\n")
		fo.close()
		return render_template("/completed_course_confirmation.html")
	else:
		return render_template("/completed_course.html")

@app.route('/new-task', methods = ['GET','POST'])
def addNewTask():
	if request.method == 'POST':
		name = request.form['taskName']
		course = request.form['course']
		category = request.form['category']
		pathName = "data/user001/" + course
		if ((os.path.isdir(pathName)) == False): # if directory does not exist
			os.mkdir(pathName) # create the directory
		pathName += "/" + name + ".txt"
		fo = open(pathName,'w')
		fo.write(name + "\n")
		fo.write(course + "\n")
		fo.write(category + "\n")
		fo.close()
		return render_template("/new_task_confirmation.html") # add 
	else:
		return render_template("/new_task.html")

@app.route('/completed-task', methods = ['GET','POST'])
def addCompletedTask():
	if request.method == 'POST':
		name = request.form['taskName']
		course = request.form['course']
		category = request.form['category']
		grade = request.form['grade']
		pathName = "data/user001/" + course
		if ((os.path.isdir(pathName)) == False): # if directory does not exist
			os.mkdir(pathName) # create the directory
		pathName += "/" + name + ".txt"
		fo = open(pathName,'w')
		fo.write(name + "\n")
		fo.write(course + "\n")
		fo.write(category + "\n")
		fo.write(grade + "\n")
		fo.close()
		return render_template("/completed_task_confirmation.html")
	else:
		return render_template("/completed_task.html")
