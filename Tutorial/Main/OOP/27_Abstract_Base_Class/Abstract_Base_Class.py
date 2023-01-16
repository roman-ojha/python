# from abc import ABCMeta, abstractmethod
# ABCMeta is the metaclass form the older version of the python
from abc import ABC, abstractmethod
# here ABC is the metaclass form the newer version of the python


class Shape(ABC):
    # if we inherit any class form ABC metaclass then this class can give an order ot the derived class to needs to implement some method in derived class that is compalsry
    @abstractmethod
    def printarea(self):
        pass
    # now this is the method that need to be made in derived class if we did't make this fundtion in derived class and define it then it will through an error
    # NOTE: we can't be able to make the object of the abstract base class

    # Defining the concrete method
    def show(self):
        print("Shape Concrete method")


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    # we must have to define the abstract base class method
    def printarea(self):
        return self.length * self.breadth


rect1 = Rectangle()
print(rect1.printarea())
rect1.show()


# EX2:
class DefenseForce(ABC):  # Abstract class
    # we can define the constructor and assign some property into it which will get share by all the class that are derived from this class
    def __init__(self) -> None:
        self.id = 101

    @abstractmethod
    def area(self):  # Abstract method
        pass

    def gun(self):  # Concrete method
        # Here it share the same concrete value for all the child class now
        print("Gun = AK")


class Army(DefenseForce):
    def area(self):
        print("Area = Land")


class AirForce(DefenseForce):
    def area(self):
        print("Area = Sky")


class Navy(DefenseForce):
    def area(self):
        print("Area = Sea")


army = Army()
air_force = AirForce()
navy = Navy()

# 'gun' method is concrete and perform the same method for all the object that derive 'DefenseForce'
army.gun()
air_force.gun()
navy.gun()

print(army.id)
print(air_force.id)
print(navy.id)

army.area()
air_force.area()
navy.area()
