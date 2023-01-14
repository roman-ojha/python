
class Employee:
    no_of_leaves = 8
    var = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


class Player:
    var = 9
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"


class CoolProgramer(Player, Employee):
    # this is the multiple inhetitance because we are inheriting from two bass class
    # here when we are deriving class from two class then then order of inherithing is important here we put player in first and Employee as second means that firstly when we made an object of the CoolProgramer first Player class constructor will call not only constructor all the method and variable will first search in Player class and if that method will not find in that class only after that it will search to the another sequencily inherited base class
    # if base class have same named method and varaiable then it will search sequencilly in here firstly it will go to Player, class and only Employee class though we have the same named method and variable Player method will call
    language = "C++"

    def printlanguage(self):
        print(self.language)


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgramer("Karan", ["Cricket"])
print(karan.var)
