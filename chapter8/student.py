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

class Student():
    def __init__(self, student_name, id_number, object_grade):
        self.student_name = student_name
        self.id_number = id_number
        self.object_grade = object_grade    
    
    def getStuden_Name(self, student_name):
        return self.student_name

    def getId_Number(self, id_number):
        return self.id_number

    def getObject_Grade(self, object_grade):
        return self.object_grade

    def __str__(self):
        return str(self.student_name) + ", " + self.id_number
