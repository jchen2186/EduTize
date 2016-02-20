from datetime import datetime as dt
#code for datetime today = datetime.date.today() 

class Assignment():
    course = null
    category = null
    deadline = null
    grade = []

    heirarchy = ["quiz","homework","lab", "test"]

    def __init__(c, t, d, g):
    self.course = c
    self.category = t
    self.deadline = d
    self.grade = g

    def compare(self, other):
        if heirarchy.index(self.category) > heirarchy.index(other.category):#if the category has a greater priority
            return(self)#returns entire assignment object
        elif heirarchy.index(self.category) < heirarchy.index(other.category):
            return(other)
        else:
            a = dt.strptime((self.deadline), "%m/%d/%y") #deadline format m/d/y
            b = dt.strptime((other.deadline), "%m/%d/%y")
            if a > b:
                return(self)
            elif b < a:
                return(other)
            else:    # if both are due on same day
             #compare the grades for each class
                 if self.grade < other.grade:
                     return(self)
                 else:
                     return(other)
