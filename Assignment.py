from Course import Course
from datetime import datetime as dt
#code for datetime today = datetime.date.today() 

heirarchy = ["quiz","homework","lab", "test"]

class Assignment:
    name = None
    course = None
    category = None
    deadline = None
    goalGrade = None
    receivedGrade = None

    def __init__(self, c, t, n):
        self.course = c
        self.category = t
        self.name = n

    def pastAssign(self, grade): # actual grade received
        self.receivedGrade = grade

    def upcomingAssign(self, deadline): # add grade argument later
        #self.goalGrade = grade <-- goal grade user wants,
        self.deadline = deadline

    def compare(self, other): # returns the assignment with higher priority
        if heirarchy.index(self.category) > heirarchy.index(other.category):#if the category has a greater priority
            return(self)#returns entire assignment object
        elif heirarchy.index(self.category) < heirarchy.index(other.category):
            return(other)
        else:
            a = dt.strptime((self.deadline), "%m/%d/%y") #deadline format mm/dd/yyyy
            b = dt.strptime((other.deadline), "%m/%d/%y")
            if a > b:
                return(self)
            elif b < a:
                return(other)
            else:    # if both are due on same day
             #compare the grades for each class
                if (self.course.currGPA < other.course.currGPA):
                    return(self)
                else:
                    return(other)