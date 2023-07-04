class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

    # Instance variable can inherit
    # Instance Method can inherit
    # Class Method can inherit
    # Static Method can inherit


class Programmer(Employee):
    # we can inhaerite Employee class like this
    # now all the property and the method of the Employee class come the the Programmer class
    # nowe we can add another method and class vaiable in hear as well
    no_of_holiday = 56
    no_of_leaves = 500
    # we can oberride the base class variable value in here as well

    def __init__(self, aname, asalary, arole, languages):
        # this constructor that we made here is different then the base class constructor
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Programmer("Shubham", 555, "Programmer", ["python"])
karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])
print(karan.no_of_holiday)
