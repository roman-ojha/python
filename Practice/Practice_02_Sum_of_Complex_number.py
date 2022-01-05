class Complex:
    def __init__(self,a=None,b=None):
        self.a=a
        self.b=b
    
    def calculation(self,c1,c2):
        self.a=c1.a+c2.a
        self.b=c1.b+c2.b
    
    def printdata(self):
        print(f"A: {self.a}\nB: {self.b}")

c1=Complex(1,2)
c2=Complex(3,4)
c3=Complex()
c3.calculation(c1,c2)
c3.printdata()
