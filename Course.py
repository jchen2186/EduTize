class Course:
	name = None
	gradeDist = None
	goalGPA = None
	currGPA = None
	assignments = None

	def __init__(self, name, goalGPA):
		self.name = name
		self.gradeDist = {}
		self.goalGPA = goalGPA
		self.assignments = [] # array that holds Assignment objects

	def addAssignment(self, assign):
		self.assignments.append(assign)

	def getGPA(self): # out of 100
		# sumCategory adds up all the grades of that category
		# numCategory adds up the number of assignments in that category
		sumQuizzes = sumHomeworks = sumLabs = sumTests = 0
		numQuizzes = numHomeworks = numLabs = numTests = 0
		for assign in self.assignments:
			if (assign.category == "quiz"):
				sumTests += assign.grade
				numTests += 1
			elif (assign.category == "homework"):
				sumHomeworks += assign.grade
				numHomeworks += 1
			elif (assign.category == "lab"):
				sumLabs += assign.grade
				numLabs += 1
			elif (assign.category == "test"):
				sumTests += assign.grade
				numTests += 1
		# find the average for each category
		quizAvg = sumQuizzes / numQuizzes
		homeworkAvg = sumHomeworks / numHomeworks
		labAvg = sumLabs / numLabs
		testAvg = sumTests / numTests
		gpa = (quizAvg * gradeDist["quiz"] +
			homeworkAvg * gradeDist["homework"] +
			labAvg * gradeDist["lab"] + 
			testAvg * gradeDist["test"]);
		return gpa;

	def setGPA(self):
		self.currGPA = getGPA(self)

	# given a syllabus, user can add how the prof calculates the grade
	def setGradeDist(self, quizPercent, homeworkPercent, testPercent):
		self.gradeDist["quiz"] = quizPercent
		self.gradeDist["homework"] = homeworkPercent
		self.gradeDist["test"] = testPercent

	# if lab is a component of the class
	def setGradeDist(self, quizPercent, homeworkPercent, testPercent, labPercent):
		self.gradeDist["quiz"] = quizPercent
		self.gradeDist["homework"] = homeworkPercent
		self.gradeDist["test"] = testPercent
		self.gradeDist["lab"] = labPercent

	def compare(self, other): # returns course with higher priority
		if (self.currGPA > other.currGPA):
			return other
		elif (self.currGPA < other.currGPA):
			return self
		else:
			return "Both courses have the same GPA"