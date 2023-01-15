# Hierarchical Inheritance
class Vehicle(object):
    info = "Create an object of the Subclass that inherit this class"

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def start(self):
        print("Started ", self.name)

    def accelerator(self):
        print("Running ")

    def press_break(self):
        print("Stopped ")

    def turn_left(self):
        print("Turning left ")

    def turn_right(self):
        print("Turning right")

    def back(self):
        print("Running backwards")

    @classmethod
    def get_vehicle_info(cls):
        print(cls.info)


class Car(Vehicle):
    def __init__(self, name, color, price, model):
        super().__init__(name=name, color=color, price=price)
        self.model = model

    def get_car_info(self):
        print("Name: ", self.name)
        print("Color: ", self.color)
        print("Price: ", self.price)
        print("Model: ", self.model)


class Truck(Vehicle):
    def __init__(self, name, color, price, model):
        super().__init__(name=name, color=color, price=price)
        self.model = model

    def get_truck_info(self):
        print("Name: ", self.name)
        print("Color: ", self.color)
        print("Price: ", self.price)
        print("Model: ", self.model)


car = Car(name="Tesla", color="Red", price="40000", model="X")
truck = Truck(name="Tesla", color="White", price="70000", model="Cyber Truck")

Vehicle.get_vehicle_info()
print("\n")

car.get_car_info()
car.start()
car.accelerator()
car.turn_right()
car.turn_left()
print("\n")

truck.get_truck_info()
truck.start()
truck.accelerator()
truck.turn_right()
truck.turn_left()
print("\n")
