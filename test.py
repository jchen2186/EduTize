import time
from Assignment import Assignment
from Course import Course

calculus = Course("Calculus",90)
calculus.currGPA = 90
english = Course("English",95)
english.currGPA = 95

mathHW = Assignment(calculus,"homework","hw 3")
print mathHW.course.name
print mathHW.category
#mathHW.pastAssign(90)
#print mathHW.receivedGrade

mathHW.upcomingAssign(95,"03/01/16")
#print mathHW.goalGrade
#print time.strptime(mathHW.deadline, "%d %b %y")

englishHW = Assignment(english,"homework","paper 2")
englishHW.upcomingAssign(100,"03/03/16")
#print englishHW.goalGrade
#print time.strptime(englishHW.deadline,"%d %b %y")

print mathHW.compare(englishHW).name
