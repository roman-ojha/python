
# Public -
# Protected -
# Private -

class Employee:
    no_of_leaves = 8
    # here this is the public variable and this is the default access specifiers
    var = 8
    _protec = 9
    # now by using one underscore "_" it become protected and it can be able to access by only object and derived class

    __pr = 98
    # now by using tow underscore this is the private variable now this variable will only be able to access inside the class

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
        # this is the public method because we did't specify any access specifiers and public is default

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    # Protected member function
    def _protected_fun(self):
        print("Protected function")

    # Private member function
    def __private_fun(self):
        print("Private function")

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


emp = Employee("harry", 343, "Programmer")

print(emp._protec)
# we can be able to access protected variable by object

print(emp.__pr)
# now in here we are trying to access private variable which will give an error
print(emp._Employee__pr)
# but like this we can be able to access private variable as well it is called as a "Name mangling"
