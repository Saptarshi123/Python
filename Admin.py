from StudentScheduler import StudentScheduler
from course import Course
from Student import Student
class Admin:
    studentScheduler=StudentScheduler()
    studentList=[]
    number=int(input("Enter the total number of students you want to add:"))
    for i in range(0,number):
        student=Student()
        student.setName(raw_input("Enter the name of the student"))
        student.setRollNumber(input("Enter the roll number of the student"))
        noOfCourses=int(raw_input("How many courses you want to add:"))
        for j in range(0,noOfCourses):
            course = Course()
            course.setCourseName(raw_input("Enter the Course"))
            student.setCourseNames(course)
        studentScheduler.addStudent(student)
        list=studentScheduler.showStudents()
        for k in range(0,len(list)):
            print(list[i])


