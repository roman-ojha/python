class Father:
    def __init__(self):
        print("Father class Constructor")

    def showF(self):
        print("Father class Method")


class Son(Father):
    def __init__(self):
        super().__init__()  # Calling Father class constructor
        print("Son class Constructor")

    def showS(self):
        print("Son Class Method")


class Daughter(Father):
    def __init__(self):
        super().__init__()  # Calling Father class constructor
        print("Daughter class Constructor")

    def showD(self):
        print("Daughter class Method")


son = Son()
# Output:
# Father class Constructor
# Son class Constructor

son.showF()
# Father class Method
son.showS()
# Son Class Method

daughter = Daughter()
# Output:
# Father class Constructor
# Daughter class Constructor

daughter.showF()
# Father class Method
daughter.showD()
# Daughter class Method
