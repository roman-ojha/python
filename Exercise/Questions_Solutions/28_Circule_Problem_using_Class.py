# Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.

PIvalue =3.141592654

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def getArea(self):
        self.area=PIvalue*self.radius*self.radius
        return self.area
    def getCircumference(self):
        self.circumference=2*PIvalue*self.radius
        return self.circumference

circle=Circle(3)
print("The area of the circle with radius 3 is:",circle.getArea())
print("The circumference of the circle with radius 3 is:",circle.getCircumference())