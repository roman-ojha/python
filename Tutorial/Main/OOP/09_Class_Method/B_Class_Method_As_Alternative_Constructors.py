class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def form_str(cls, string):
        params = string.split("-")
        # here get the string and we can split that string and can be able to make it as an list which will store the value of the object
        return cls(params[0], params[1], params[2])
        # now here we can be  able to return the split string to the constructor that become the value of the object

    # the Alternative method to do this is
    @classmethod
    def form_str2(cls, string):
        return cls(*string.split("-"))
        # we can return arg as well


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", "455", "Student")
harry.change_leaves(34)
# we can see that when change the value of change_leaves form one object then also the another object change_leaves value will also changed and overall class variable value will changed which means that it is changing the class variable not the instance variable
print(harry.no_of_leaves)
print(Employee.no_of_leaves)

karan = Employee.form_str("karan-480-student")
# to pass the default constructor we can particularly can say that which funciton you want to call while making an object
print(karan.salary)
# now we get the salary of the karan through the string and spliting that string

# the Alternative metnod
hari = Employee.form_str2("hari-545-student")
print(hari.salary)
