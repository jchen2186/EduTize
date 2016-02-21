from flask import render_template, request
from app import app
import sys
import os
from os import listdir
from os.path import isfile, join

@app.route('/')

@app.route('/index')
def index():
	pathName = "data/user001"
	dataFiles = os.listdir(pathName) # list of directories
	fileData = {} # dictionary with key: [val1,val2,val3...]
	for course in dataFiles: # course is a directory
		pathName += directory + "/upcoming/"

		for category in os.listdir(pathName): # directory in upcoming
			pathName += category
			for assignment in os.listdir(pathName):
				f = open(pathName + "/" + assignment,"r")
				# name = f.readline()
				# course = f.readline()
				# category += f.readline()
				fileData[assignment] = [category,course]
			pathName = "data/user001/" + course + "/" + "upcoming" + "/"
		pathName = "data/user001"

	# prioritize based on category, then deadline, then course's gpa
	heirarchy = ["test","lab","homework","quiz"] # category
	pathName = "date/user001"
	dataFiles = os.listdir(pathName) # list of directories
	for course in dataFiles: # course is a directory
		pathName += directory + "/upcoming/"

		for category in os.listdir(pathName): # directory in upcoming
			pathName += category
			for assignment in os.listdir(pathName):
				f = open(pathName + "/" + assignment,"r")
				# name = f.readline()
				# course = f.readline()
				# category += f.readline()
				fileData[assignment] = [category,course]
			pathName = "data/user001/" + course + "/" + "upcoming" + "/"
		pathName = "data/user001"
	# organizedByCategory = []
	# priority1, priority2, priority3 = 0
	# priority1 = fileData[f]
	# for f in fileData: # f is a key
	# 	priority1 = f


	fo = open("app/templates/index.html","w")
	fo.write("""
	{% extends "base.html" %}

	{% block title %} Home {% endblock %}

	{% block body %}
	<div id= "content">

	<!--1 table, 2 columns;-->

	<table width="100%">
		<tr>
			<td class ="ranking">
				1
			</td>
			<td class = "assignment">
				<!--insert assignment name--><br>
				<!--insert course name--><br>
				<!--insert type --><br>
				<!--insert due date-->
			</td>
		</tr>

		<tr>
			<td class ="ranking">
				2
			</td>
			<td class = "assignment">
				<!--insert assignment name--><br>
				<!--insert course name--><br>
				<!--insert type --><br>
				<!--insert due date-->
			</td>
		</tr>

		<tr>
			<td class ="ranking">
				3
			</td>
			<td class = "assignment">
				<!--insert assignment name--><br>
				<!--insert course name--><br>
				<!--insert type --><br>
				<!--insert due date-->
			</td>
		</tr>

	</table>

	</div>
	{% endblock %}""")
	fo.close()
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

		f1 = open("app/templates/new_course_confirmation.html", "w")
		f1.write(""" {% extends "base.html" %}

		{% block title %} Confirming New Course {% endblock %}

		{% block body %}
		<div id= "content">

		<h1>Your course has been recorded!</h1>
		<h2>Course: """ + course + """ </h2>
		<h2>Goal GPA: """ + gpa + """ </h2>

		</div>

		{% endblock %} """)
		f1.close()
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

		f1 = open("app/templates/completed_course_confirmation.html", "w")
		f1.write(""" {% extends "base.html" %}

		{% block title %} Confirming New Course {% endblock %}

		{% block body %}
		<div id= "content">

		<h1>Your course has been recorded!</h1>
		<h2>Course: """ + course + """ </h2>
		<h2>Goal GPA: """ + gpa + """ </h2>

		</div>

		{% endblock %} """)
		f1.close()
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
		if ((os.path.isdir(pathName)) == False): # if course directory does not exist
			os.mkdir(pathName) # create the directory
		pathName += "/" + "upcoming"
		if ((os.path.isdir(pathName)) == False):
			os.mkdir(pathName)
		pathName += "/" + category
		if ((os.path.isdir(pathName)) == False): # if category directory does not exist
			os.mkdir(pathName) # create the directory
		pathName += "/" + name + ".txt"
		fo = open(pathName,'w')
		fo.write(name + "\n")
		fo.write(course + "\n")
		fo.write(category + "\n")
		fo.close()

		f1 = open("app/templates/new_task_confirmation.html", "w")
		f1.write(""" {% extends "base.html" %}

		{% block title %} Confirming New Course {% endblock %}

		{% block body %}
		<div id= "content">

		<h1>Your course has been recorded!</h1>

		<h2>Task: """ + name + """</h2>
		<h2>Course: """ + course + """</h2>
		<h2>Type: """ + category + """</h2>

		</div>

		{% endblock %} """)
		f1.close()
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
		pathName += "/" + "past"
		if ((os.path.isdir(pathName)) == False):
			os.mkdir(pathName)
		pathName += "/" + category
		if ((os.path.isdir(pathName)) == False): # if category directory does not exist
			os.mkdir(pathName) # create the directory
		pathName += "/" + name + ".txt"
		fo = open(pathName,'w')
		fo.write(name + "\n")
		fo.write(course + "\n")
		fo.write(category + "\n")
		fo.write(grade + "\n")
		fo.close()

		f1 = open("app/templates/completed_task_confirmation.html", "w")
		f1.write(""" {% extends "base.html" %}

		{% block title %} Confirming New Course {% endblock %}

		{% block body %}
		<div id= "content">

		<h1>Your course has been recorded!</h1>

		<h2>Task: """ + name + """</h2>
		<h2>Course: """ + course + """</h2>
		<h2>Type: """ + category + """</h2>
		<h2>Grade: """ + grade + """</h2>

		</div>

		{% endblock %} """)
		f1.close()

		return render_template("/completed_task_confirmation.html")
	else:
		return render_template("/completed_task.html")
