class Father:
    def __init__(self):
        super().__init__()  # Calling Parent class Constructor
        # This will call the 'object' class constructor
        # and 'object' class constructor will call all child class constructor except this class
        # because it is already been visit
        print("Father class constructor")

    def showF(self):
        print("Father class Method")


class Mother:
    def __init__(self):
        super().__init__()  # Calling Parent class Constructor
        # 'object' class constructor will call 'Mother' class construct
        print("Mother class constructor")

    def showM(self):
        print("Mother class Method")


class Son(Father, Mother):
    def __init__(self):  # Overriding base class constructor
        # Calling base class constructor
        super().__init__()  # Calling Parent class Constructor
        # But we know that we have to Base class 'Father' & 'Mother'
        # It will only call 'Father' class constructor
        # Because we have inherit from 'Father' before 'Mother'
        # (Mother, Father) : here we are inheriting 'Mother' before 'Father'
        print("Son class constructor")

    def showS(self):
        print("Son class Method")


son = Son()
# Output:
# Mother class constructor
# Father class constructor
# Son class constructor

son.showF()
# Father class Method

son.showM()
# Mother class Method

son.showS()
# Son class Method
