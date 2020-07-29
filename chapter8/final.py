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
    def __init__(self, student_name, id_number):
        self.student_name = student_name
        self.id_number = id_number
           
    def getStuden_Name(self, student_name):
        return self.student_name

    def getId_Number(self, id_number):
        return self.id_number

    def getObject_Grade(self, object_grade):
        return self.object_grade

    def __str__(self):
        return str(self.student_name) + ", " + str(self.id_number)

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

def main():
    student=Student("Jesus Rodriguez", 98012345565) 
    c1=Grade(input("Class name: "), int(input("Credits: ")), float(input("Grades: ")))
    c2=Grade(input("Class name: "), int(input("Credits: ")), float(input("Grades: ")))
    c3=Grade(input("Class name: "), int(input("Credits: ")), float(input("Grades: ")))
    gpa =  ((c1.class_credits * c1.grade_points) + (c2.class_credits * c2.grade_points) + (c3.class_credits * c3.grade_points)) / (c1.class_credits + c2.class_credits + c3.class_credits) 
    print("---------------------------------")
    print("The student name is: ", student.student_name)
    print("The student ID is : ", student.id_number)
    print("---------------------------------")
    print("Course" ,"\t","\t", "Grade" ,"\t","\t", "Credits")
    print(c1.class_name, "\t", "\t", c1.grade_points, "\t", "\t", c1.class_credits)
    print(c2.class_name, "\t", "\t", c2.grade_points, "\t", "\t", c2.class_credits)
    print(c3.class_name, "\t", "\t", c3.grade_points, "\t", "\t", c3.class_credits)
    print("\t", "\t",c1.grade_points + c2.grade_points + c3.grade_points,"\t", "\t",(c1.class_credits * c1.grade_points) + (c2.class_credits * c2.grade_points) + (c3.class_credits * c3.grade_points))
    print("Your GPA is : ", gpa)
    
main()

    
