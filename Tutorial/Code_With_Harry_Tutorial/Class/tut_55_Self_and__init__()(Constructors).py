# Self is that class where the function is implemeting of invoke
class Employee:
    no_of_leaves = 8

    def __init__(self):
        pass
    # this is the default constructor
    
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


# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
# we can pass these value as an argument
harry = Employee("Harry", 255, "Instructor")
# this is the way call the constructor
# this will automatically called when we make an object
print(harry.salary)
# now we can call


# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"
# print(rohan.printdetails())
# here in printdetails() argument rohan will pass and if rohan have his instance variable called name,salary and role then self.name will going to have the name stored in instance variable
# another thing is that in printdetaile if also that function doesnot have an argument when you call it then also rohan will automatically go as an argument so we have to handel that argument that's why we use self we get that rohan argument so we have to use self to hold that default argument
