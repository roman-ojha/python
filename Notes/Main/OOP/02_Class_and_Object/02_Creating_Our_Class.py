# Example 1:
# here we are making a class
class Student:
    pass


# we are making an object from student class
harry = Student()
larry = Student()

# we can make instance variable of an object like this
harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["hindi", "physics"]
print(harry.name, harry.std)
print(harry.section, larry.subjects)
# if we will going to use 'larry.name' then it will through an error because we did not define the name for the larry


# Example 2:
class MyClass(object):
    # Every class derived from the based class 'object'
    # Not recommended to use 'object' while defining the class
    def show(self):
        # every class method will given us the 'self' instance object
        print("Hello world")


obj = MyClass()
obj.show()


# Example 2:
class Mobile:
    # writing our one constructor which get called whenever we create the object
    def __init__(self):
        self.model = "RealMe"

    def show_model(self):
        print("Model: ", self.model)


realMe = Mobile()
# Accessing method
realMe.show_model()
# Accessing properties
print(realMe.model)
# Updating property value
realMe.model = "RealMe Pro2"
print(realMe.model)


# EXample 4:
class Mobile2:
    # writing our one constructor which get called whenever we create the object
    def __init__(self, model):
        self.model = model

    def show_model(self, price):
        print("Model: ", self.model, " Price: ", price)


realMe2 = Mobile2("RealMe X")
realMe2.show_model(30000)
print("Address of realMe2: ", id(realMe2))
# Address of realMe2:  3058544135760

readMi = Mobile2("ReadMi 7s")
readMi.show_model(20000)
print("Address of readMi: ", id(readMi))
# Address of readMi:  3058544135952


# Example 5:
class Employee:
    no_of_leaves = 8
    # this is the class variable
    pass


harry = Employee()
rohan = Employee()


harry.name = "Harry"
harry.salary = 455
harry.role = "instructor"
print(harry.name, harry.salary)
# the variable that we made in here like name,salary,role these variable are the instance variable of an object not the varialbe of the class
print(harry.no_of_leaves)
# but here no_of_leaves is the is the property of the class
print(Employee.no_of_leaves)
# so we can access variable inside the class through the class as well
# if we want to change the value the variable of class we can do that through class name
Employee.no_of_leaves = 9
# we can change the value of the no_of_leaves thorugh but!!!
harry.no_of_leaves = 10
# here we are trying to change the value of the class variable then it cant be able to change
# but!!! we are acctully making the new instance variable of an object
print(harry.no_of_leaves)
# we can varify through one attribute and that is:
print(harry.__dict__)
# __dict is defined in all classes and it return dictionary
# now we can see that now no_of_leaves is the instance variable of an object
print(Employee.__dict__)


rohan.name = "Rohan"
rohan.salary = 455
rohan.role = "Student"
print(rohan.name, rohan.salary)
print(rohan.no_of_leaves)
# but for rohan object no_of_leaves is not the instance variable but the class variable
