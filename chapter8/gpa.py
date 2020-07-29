'''
Jesus Manuel Rodriguez Castro
12/04/2019
Assigment 8 Data Collections


*Create a class called Grade that contains the class name,
 the credits and the grade point (from 0 to 4) for the grade.

*Create a second class called Student that contains the students
 name and id number and a list of grade objects.

*The student class should have a methods to enter the name and id,
 and a method to calculate a GPA.

*(GPAs are what is called "weighted averages." To calculate a
 GPA you get a weight by multiplying the grade by the credits.
 Then you divide the sum of the weights by the sum of the credits.)

*There should be a display class that allows you to enter the
 information into the grade and student classes and then displays
 the student name, id and the GPA.

*This is complex enough that I don't have an extra credit.
'''

class Gpa():
    def __init__(self, student):
        self.student=student
        self.clas=[]

    def addclas(self, clas):
        self.clas.append(self.clas)

    def totalClasses(self):
        total=0
        for clas in self.clas:
            return total

    def totalCredits(self):
        total=self.totalClasses()
        credit = total
        return credit

    
            
        
            
            
