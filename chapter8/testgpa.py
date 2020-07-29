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

from student import Student
from grade import Grade
from gpa import Gpa

    
def main():
    student1 = Student("Jesus Rodriguez", "98102121", "15")
    c= Gpa(1)
    cont= "y"
    while cont == "y":
        enterclass=input("Enter name of the class:" )
        entercredits= int(input("Enter how many credits the class weight: "))
        entergrade = float
        (input("Enter grade that you got in the class: "))
        clas= Grade(enterclass, entercredits, entergrade)
        c.addclas(clas)
        cont= input("To add another class press y: ")
    print(Student("jesus", "98102121", "15"))
    print(c)
        
        

        
    
    
  
   
    
main()
