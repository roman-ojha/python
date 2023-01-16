# @property decorator is a built-in decorator in Python which is helpful in defining the properties effortlessly without manually calling the inbuilt function property(). Which is used to return the property attributes of a class from the stated getter, setter and deleter as parameters.
# Have three method of @property
# 1. getter - to access the value of the attribute.
# 2. setter - to set the value of the attribute.
# 3. deleter - to delete the instance attribute.


# EX1:
class Portal:
    def __init__(self):
        self.__name = ''  # Private variable
        # '__name' can't be able to access outside of the class

    @property  # @property method
    def name(self):  # Getter Method
        # now we can be able to access the 'name' property from outside the class

        # here we can return what ever we want
        # but we can access the property 'name' with '.' operator
        return self.__name

    @name.setter  # Setter method
    def name(self, name):
        # Now we can set any property using instance object using =
        # EX: obj.name = "Roman"

        self.__name = name

    @name.deleter
    def name(self):
        # using ths we can delete the instance variable
        # deleting using object
        # EX: del obj.name

        del self.__name


p = Portal()

# setting name
p.name = "Roman"  # call setter 'name' function

# Getting name
print(p.name)  # call getter 'name' function

# Deleting name
del p.name  # call deleter 'name' function


# EX2:
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


employee1 = Employee("Razz", "Roman")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

# print(employee1.email)

# if we will try to change the 'fname' of 'employee1' then it will not going to change because we pass the value and construct it
# employee1.fname = "US"

# print(employee1.fname)

# print(employee1.email)
# after setting fname="US"  also the fname of the employee1 will not change this problem will solved by the setters
# now this will change the email
# print(employee1.email())
# but this will not follow encapsulation that's why we use property decorator
# print(employee1.email)
# now it will take email as a proporty

# employee1.email = "this.that@gmail.com"
# print(employee1.fname)

# del employee1.email
# # you cant delete email you have to make @email.deleter
# print(employee1.email)
# employee1.email = "Harry.Perry@gmail.com"
# print(employee1.email)
