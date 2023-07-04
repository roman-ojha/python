class Father:
    def __init__(self):  # Constructor
        self.money = 1000  # Instance member variable
        print("Father class Constructor")

    def show(self):
        print("Father class Instance Method")


class Son(Father):
    # If we will not create the '__init__' constructor inside this class
    # then while creating the object of 'Son' it will call the '__init__' constructor of Parent 'Father' class

    def desc(self):
        print("Son Class Instance Method")


son = Son()
# Father class Constructor

money = son.money
print("Money of Son: ", money)
# Money of Son:  1000

son.show()
# Father class Instance Method

son.desc()
# Son Class Instance Method

# Passing Argument into Parent class constructor


class Father2:
    def __init__(self, money):
        # Because here we are getting the 'money' parameter
        # But if we will create the 'Son2' object in that case we have to pass the parameter for this constructor
        self.money = money
        print("Father class Constructor")

    def show(self):
        print("Father class Instance Method")


class Son2(Father2):

    def desc(self):
        print("Son Class Instance Method")

    def show_money(self):
        print("Money of Son2: ", self.money)


son2 = Son2(3000)
print("Money of Son2: ", son2.money)
son2.show_money()
