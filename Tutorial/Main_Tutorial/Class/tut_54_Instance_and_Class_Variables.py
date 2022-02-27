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
