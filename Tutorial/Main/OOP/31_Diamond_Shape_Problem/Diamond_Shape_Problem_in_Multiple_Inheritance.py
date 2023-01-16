# python by default solved the diamond shape problem

class A:
    def met(self):
        print("This is a method from class A")


class B(A):
    def met(self):
        print("This is a method from class B")


class C(A):
    def met(self):
        print("This is a method from class C")


class D(C, B):
    # If we don't define the 'met' method in this class then it will call the 'met' method of class 'C'

    # Overriding the 'met' method
    # def met(self):
    #     print("This is a method from class D")
    pass


a = A()
b = B()
c = C()
d = D()

d.met()
