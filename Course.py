class Course():

	def __init__(self, name, gradeDist, currGPA, goalGPA):
		self.name = name
		self.gradeDist = gradeDist
		self.currGPA = currGPA
		self.goalGPA = goalGPA

	def getCourse(self):
		return self.name;

	def getGradeDist(self):
		return self.gradeDist

	def getCurrGPA(self):
		return self.currGPA

	def getGoalGPA(self):
		return self.goalGPA
