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

class Student():
    def __init__(self, student_name, id_number, object_grade):
        self.student_name = student_name
        self.id_number = id_number
        self.object_grade = object_grade

    def __str__(self):
        return str(self.student_name) + ", " + self.id_number
    
    
       
gpa = Grade(eval(input("Enter name: ")), eval(input("Enter credit: ")), eval(input("Enter points: ")))