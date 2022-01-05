
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        # this is the way to make a constructor
        # in self the object we are making will come
        self.name = aname
        # here self.name , name is the instance variable name
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        # self is the object which call this function
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    # here we are using classmethod decorator
    @classmethod
    def change_leaves(cls, new_leaves):
        # we can make the class method so that we dont have to take self
        # cls is that class which instance is that object which run the function of the class
        cls.no_of_leaves = new_leaves


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", "455", "Student")
harry.change_leaves(34)
# we can access class method throung instance and class as well

print(harry.no_of_leaves)
print(Employee.no_of_leaves)
Employee.change_leaves(40)
print(rohan.no_of_leaves, " ", rohan.salary)
# NOTE: we can only make the instace variable of the Object as well we can make the class variable of the object which in which instance varable is only the variable of the one object but class variable is the variable of all object

# Employee.no_of_leaves = 89

# NOTE: if we use normal method in class then self will be an default argument but if we dont want to use self then we use class method
