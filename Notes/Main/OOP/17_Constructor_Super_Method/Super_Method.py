
class A:
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"
        # all of these are the instance variable


class B(A):
    classvar1 = "I am in class B"
    # when we want to access classvar1 through class B then firstly it will search instance variable of the derived class if it will not find the instance variable of the derived class then it will go to the inherit class(base class) and search there do that class have instance variable if it will have then it will access value form that instance variable if the base class doesnot have instance variabel then it will search the class variabel of the derived class and only if it will not find the class variable in the derived class then it will search class variable of the base class
    # -> step : derived instance -> base instance -> derived class variable -> base class variable
    # this is called as an overriding

    # def __init__(self):
    #     self.var1 = "I am inside class B's constructor"
    #     self.classvar1 = "Instance var in class B"
    #     self.special = "Special"
    # here we override constructor

    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        # super().__init__()
        # we are calling the supper class(base class) conatructor
        # print(super().classvar1)
        # we can call base class constructor instance variable like this


a = A()
b = B()


print(b.special)
# by using super now we can be abel to access instance variabel of base class

print(b.var1)
# but in here derived class instance variable override the base class instance variable but if we will use super() and call base class consturcto in the last line of the derived constructor then base class constructor override the derive class instance variable because firstly derived class instance variable will override the base class instance variable and after that we call super() in here again base class constructor will call and override the derived class instance variable

print(b.classvar1)
