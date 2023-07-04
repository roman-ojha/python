# Passing Member of one class to Another Class

class Student:
    # Constructor
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    # Instance method
    def desc(self):
        print("Student Name: ", self.name)
        print("Student Roll: ", self.roll)


class User:
    # Creating Static method and getting another class object
    @staticmethod
    def show(student: Student):
        print("Student Name: ", student.name)
        print("Student Roll: ", student.roll)


student = Student("Roman", 25)
user = User()
# Passing the 'student' object into 'user' object inside static method
user.show(student=student)
