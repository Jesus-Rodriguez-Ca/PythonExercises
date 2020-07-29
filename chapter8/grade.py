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

class Grade():
    def __init__(self, class_name, class_credits, grade_points):
        self.class_name = class_name
        self.class_credits = class_credits
        self.grade_points = grade_points

    def ClassName(self,class_name ):
        return self.class_name

    def Class_Credits(self,class_credits):
        return self.class_credits

    def Grade_Credits(self, grade_points):
        return self.grade_points


 

