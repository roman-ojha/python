class Dad:
    basketball = 6

    def __init__(self):
        print("Dad class constructor")

    def showD(self):
        print("Dad class show method")


class Son(Dad):
    dance = 1
    basketball = 9

    def __init__(self):
        # Calling parent class constructor
        super().__init__()
        print("Son class constructor")

    def isDance(self):
        return f"Yes I dance {self.dance} no of times"

    def showS(self):
        print("Son class show method")


class Grandson(Son):
    dance = 6
    guitar = 1

    def __init__(self):
        # Calling parent class constructor
        super().__init__()
        print("Grandson class constructor")

    # overriding base class method
    def isDance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

    def showG(self):
        print("Grandson class show method")


g = Grandson()
# Dad class constructor
# Son class constructor
# Grandson class constructor

g.showD()
# Dad class show method
g.showS()
# Son class show method
g.showG()
# Grandson class show method
