class Mobile:
    def __init__(self, m):
        self.model = m  # Instance variable

    def get_model(self):  # Accessor/Getter Method
        return self.model

    def set_model(self, m):  # Mutator/Setter Method
        self.model = m


realMe = Mobile("RealMe X")
print(realMe.get_model())
# RealMe X
realMe.set_model("RealMe 2")
print(realMe.get_model())
# RealMe 2
