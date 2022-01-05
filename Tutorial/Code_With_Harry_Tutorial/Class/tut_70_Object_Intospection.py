
import inspect

# in python all the thing are object like int,str
# Object intospection means to know about the object that form which class it come and what is the type of that object


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

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


skillf = Employee("Skill", "F")
# print(skillf.email)
o = "this is a string"
# print(dir(skillf))
# form this we can know that this function is form __main__ function of Employe class

print(type("This is the string"))
# here we can know that this this string is come from class

# print(id("that that"))
# id will give the id of the object
# every object has it's unique id

o = "This is the string"
# print(dir(o))
# this will give all the method that we can apply in this object

print(dir(skillf))
# this will also give all the function of the skillf

# print(inspect.getmembers(skillf))
# inspect is the modiul in which getmembers will return all the members of the object
