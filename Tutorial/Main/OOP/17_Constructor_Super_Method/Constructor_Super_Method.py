class Father:
    def __init__(self):
        self.money = 1000
        print("Father class Constructor")

    def show(self):
        print("Father class Instance Method")


class Son(Father):
    # Overriding Parent class constructor
    def __init__(self):
        super().__init__()  # Calling Parent class constructor
        print("Son class Constructor")

    def desc(self):
        print("Son Class Instance Method")


son = Son()
# Output:
# Father class Constructor
# Son class Constructor

money = son.money
print("Money: ", money)
# Money:  1000

# Constructor Super method with argument:


class Father2:
    def __init__(self, money):
        self.money = money
        print("Father2 class Constructor")

    def show(self):
        print("Father2 class Instance Method")


class Son2(Father2):
    # It's child class duty to pass argument to parent class constructor using super
    def __init__(self, money, job):
        # Here we will get the 'money' while creating 'Son2' object
        # now we will pass that 'money' into the parent class constructor
        super().__init__(money)
        self.job = job
        print("Son2 class Constructor")

    def desc(self):
        print("Son2 Class Instance Method")


son2 = Son2(33000, "Python")
# Output:
# Father class Constructor
# Son class Constructor

money = son2.money
print("Money: ", money)
# Money:  33000

job = son2.job
print("Job: ", job)
# Job: Python
