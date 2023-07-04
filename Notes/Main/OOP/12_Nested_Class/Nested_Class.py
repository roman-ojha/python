class Army:  # Outer Class
    def __init__(self):
        self.name = "Roman"
        # Creating and object of 'Gun' for instance variable of 'Army'
        self.gun = self.Gun()

    def show(self):
        print("Name: ", self.name)

    class Gun:  # Inner Class
        def __init__(self):
            self.name = "AK47"
            self.capacity = "74 Rounds"
            self.length = "34.3 in"

        def desc(self):
            print(self.name, " ", self.capacity, " ", self.length)
    # NOTE: we make nested class when we want to represent inner class only for the outer class
    # Like in that case we want to create 'Gun' object for 'Army' class


army = Army()
army.show()
army.gun.desc()


# We can also create the object of inner class here
gun = Army().Gun()
