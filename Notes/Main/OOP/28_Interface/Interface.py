from abc import ABC, abstractmethod


# EX1:
class Father(ABC):  # Interface
    # We can only define @abstracemethod
    @abstractmethod
    def desc(self):
        pass

    @abstractmethod
    def desc2(self):
        pass


class Child(Father):  # Normal Class
    # We must have to define abstract method that exist on Parent class
    def desc(self):
        print("Child class Desc method")

    def desc2(self):
        print("Child class Desc2 method")


# father = Father() # Can't create object of Interface

child = Child()
child.desc()


# EX2:
class Father2(ABC):  # Interface
    # We can only define @abstracemethod
    @abstractmethod
    def desc(self):
        pass

    @abstractmethod
    def desc2(self):
        pass


class Child2(Father2):  # Abstract class
    # here we are only defining one method
    # so we can't be able to create object of this class
    # and this 'desc' method will called as concrete method
    def desc(self):
        print("Child class Desc method")


class GrandChild2(Child2):  # Normal class
    # defining the parent abstract method here
    def desc2(self):
        print("Child class Desc2 method")


# father = Father2() # Can't create object of Interface
# child = Child2() # Can't create object of Abstract class
grandSon = GrandChild2()
grandSon.desc()
grandSon.desc2()
