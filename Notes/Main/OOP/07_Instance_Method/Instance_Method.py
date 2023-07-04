class Mobile:
    def __init__(self, model):
        self.model = model  # Instance Variable

    def show_model(self, p):  # Instance Method
        self.price = p  # Instance variable
        print("Model: ", self.model, " Price: ", self.price)


realMe = Mobile("RealMe X")
realMe.show_model(30000)
# when we call the 'show_method' for 'realMe' object that automatically python will pass the address of this object as 'self' into the 'show_model' parameter
