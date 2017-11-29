from course import Course
class Student:
 courseNames=[]
 def getRollNumber(self):
    return self.rollNumber;
 def setRollNumber(self,rollNumber):
    self.rollNumber=rollNumber;
 def getName(self):
    return self.name;
 def setName(self,name):
    self.name=name;
 def getCourseNames(self,course):
     return self.courseNames
 def setCourseNames(self,course):
     self.courseNames.append(course)

 def __repr__(self):
     print("name:",self.name, "roll number:", self.rollNumber, "Course Name:", self.courseNames)
     return ""
