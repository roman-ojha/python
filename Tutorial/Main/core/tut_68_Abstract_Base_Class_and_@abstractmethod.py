
# from abc import ABCMeta, abstractmethod
# ABCMeta is the metaclass form the older version of the python
from abc import ABC, abstractmethod
# here ABC is the metaclass form the newer version of the python


class Shape(ABC):
    # if we inherit any class form ABC metaclass then this class can give an order ot the derived class to needs to implement some method in derived class that is compalsry
    @abstractmethod
    def printarea(self):
        return 0
    # now this is the method that need to be made in derived class if we did't make this fundtion in derived class and define it then it will through an error
    # NOTE: we can't be able to make the object of the abstract base class


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth


rect1 = Rectangle()
print(rect1.printarea())
