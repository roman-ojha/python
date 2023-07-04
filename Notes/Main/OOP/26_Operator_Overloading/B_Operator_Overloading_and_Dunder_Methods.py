
class Employee:
    no_of_leaves = 8
    # the method start form underscore underscore'__' and end's with underscore underscore '__' is called Dunder Method

    def __init__(self, aname, asalary, arole):
        # so this is called as dunder init
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        # this is called as dunder add which will help to do operator overloading and help to add two object variables
        return self.salary + other.salary

    def __truediv__(self, other):
        # https://docs.python.org/3/library/operator.html
        # this is same as the __add__ but it perform division
        # NOTE: we can go to the internet and search for "Mapping Operators to Function" there you can find the dunder method that which method perform what operation
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


emp1 = Employee("Harry", 345, "Programmer")
emp2 = Employee("Rohan", 55, "Cleaner")
print(emp1 + emp2)
# in here we can se that we did emp1+emp2 where this is called as operator overloading where python doesn't recognize that what kind of the perform he have to take to calculate the information but when we make __add__ method then it will perform an calculation
print(emp1 / emp2)

print(emp1)
# firstly it will perform to run __str__ method
# and secondly if __str__ method is not exist then this will call __repr__ method
print(repr(emp1))
# then this will run __repr__ method
print(str(emp1))
# and this will also run __ str__method if __str__doesn't exist then __repr__ will run
