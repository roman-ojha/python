class Father:
    def __init__(self):  # Constructor
        self.money = 1000  # Instance member variable
        print("Father class Constructor")

    def show(self):
        print("Father class Instance Method")


class Son(Father):
    # Overriding Parent class constructor
    def __init__(self):
        self.money = 5000
        self.car = "BMW"
        print("Son class Constructor")

    def desc(self):
        print("Son Class Instance Method")


s = Son()
# Output: Son class Constructor

money = s.money
car = s.car
print("Son Money: ", money, " Car: ", car)
# Son Money:  5000  Car:  BMW


# Constructor overriding with parameter
# class Father:
class Father2:
    def __init__(self, money):  # Constructor
        self.money = money  # Instance member variable
        print("Father2 class Constructor")

    def show(self):
        print("Father2 class Instance Method")


class Son2(Father2):
    # Overriding Parent class constructor
    def __init__(self, money):
        self.money = money
        self.car = "BMW"
        print("Son2 class Constructor")

    def desc(self):
        print("Son2 Class Instance Method")


s = Son2(33000)
# Output: Son2 class Constructor

money = s.money
car = s.car
print("Son2 Money: ", money, " Car: ", car)
# Son2 Money:  33000  Car:  BMW
