class User:
	pastCourses = None
	currCourses = None
	overallGPA = None
	goalGPA = None

	def __init__(self, courses, goalGPA):
		self.courses = {}
		self.goalGPA = goalGPA

	def getOverallGPA(self):
		sumGrades = numGrades = 0
		for c in self.pastCourses:
			sumGrades += pastCourses[c]
			numGrades += 1
		return sumGrades / numGrades