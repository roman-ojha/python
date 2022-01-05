"""
 Q) Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes. Print all the attributes of student1, student2 instances with their values in the given format.
"""

class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def setMarks(self,physic,math,chemistry,biology,english):
        self.physic=physic
        self.math=math
        self.chemistry=chemistry
        self.biology=biology
        self.english=english

    def printDetail(self):
        print("Student Detail:")
        total_Mark=self.physic+self.math+self.chemistry+self.biology+self.english
        print("ID",self.id,"\nName:",self.name,"\nPhysic:",self.physic,"\nMath:",self.math,"\nChemistry:",self.chemistry,"\nBiology:",self.biology,"\nEnglins:",self.english,"\nTotal Marks:",total_Mark,"\nPercentage:",str(total_Mark/5)+"%")

    
student1=Student("V12","RomanOjha")
student1.setMarks(70,80,90,79,85)
student1.printDetail()