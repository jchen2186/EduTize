class Course:

	def __init__(self, name, goalGPA):
		self.name = name
		self.gradeDist = {}
		self.currGPA = None
		self.goalGPA = goalGPA
		assignments = [] # array that holds Assignment objects

	def addAssignment(self, assign):
		self.assignments.append(assign)

	def getGPA(self):
		''' variables for sum and num for each category
		are created in order to find averages for each '''
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

	def setGradeDist(quizPercent, homeworkPercent, labPercent, testPercent):
		gradeDist["quiz"] = quizPercent
		gradeDist["homework"] = homeworkPercent
		gradeDist["lab"] = labPercent
		gradeDist["test"] = testPercent

	def compare(self, other): # returns course with higher priority
		if (getGPA(self) > getGPA(other)):
			return other
		elif (getGPA(self) < getGPA(other)):
			return self
		else:
			return "Both courses have the same GPA"