import time
from Assignment import Assignment
from Course import Course

calculus = Course("Calculus",90)
calculus.currGPA = 90
mathHW = Assignment(calculus,"homework","hw 3") # course, category, name
calculus.addAssignment(mathHW)

english = Course("English",95)
english.currGPA = 95
englishHW = Assignment(english,"homework","hw 1")
english.addAssignment(english)

mathHW.upcomingAssign(95,"03/01/16") # goal grade, deadline
englishHW.upcomingAssign(100,"03/03/16")

print mathHW.compare(englishHW).name # get the name of the assignment
										# with the higher priority

calculus.setGradeDist(90, 90, 90, 90)