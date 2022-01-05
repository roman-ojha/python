# if we use normal method in class then self will be an default argument but if we dont want to use self then we use class method which will tack class as an argument if we dont want both of instance variable and class method as an argument then we use static mathods


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
        return cls(params[0], params[1], params[2])

    @staticmethod
    def printgood(string):
        print(f"this is good {string}")
        return "thanga"
    # this is the static function which doesnot take any instance variable in default and class it is indipendent, we can say that this is the normal function like other function othside the class but if we want to pack normal function like in class then we have to use staticmethod for that and if we dont want to give the access to all the variabel we made static method, static method will only be able to access by object and class


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", "455", "Student")
harry.change_leaves(34)
print(harry.no_of_leaves)
print(Employee.no_of_leaves)
karan = Employee.form_str("karan-480-student")
print(karan.salary)
karan.printgood("thing")
# we are accessing static variable
print(karan.printgood("staff"))
Employee.printgood("Rohan")
