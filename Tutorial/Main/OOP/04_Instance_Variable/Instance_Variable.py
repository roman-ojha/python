class Mobile:
    def __init__(self):
        self.model = "RealMe X"  # Instance Variable

    def show_model(self):
        print(self.model)  # Accessing Instance Variable Inside class


realMe = Mobile()
model = realMe.model  # Accessing Instance Variable Outside Class
