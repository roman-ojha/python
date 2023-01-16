# EX1:
class House:
    def __init__(self, price):
        # first you have 'price' public instance variable
        # with it's getter(get_price) & setter(set_price) function
        self.price = price
        # But after that you want to change the 'price' public variable to '_price' protected variable
        # in that case first we have to make variable protected after that we have to change it into getter & setter function
        self._price = price

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price


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
employee1.fname = "US"

print(employee1.fname)

print(employee1.email)
# after setting fname="US"  also the fname of the employee1 will not change this problem will solved by the setters
# now this will change the email
# print(employee1.email())
# but this will not follow encapsulation that's why we use property decorator
# print(employee1.email)
# now it will take email as a proporty

employee1.email = "this.that@gmail.com"
print(employee1.fname)

del employee1.email
# you cant delete email you have to make @email.deleter
print(employee1.email)
employee1.email = "Harry.Perry@gmail.com"
print(employee1.email)
