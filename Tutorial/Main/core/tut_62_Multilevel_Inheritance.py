
class Dad:
    basketball = 6


class Son(Dad):
    dance = 1
    basketball = 9

    def isdance(self):
        return f"Yes I dance {self.dance} no of times"


class Grandson(Son):
    dance = 6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"
    # you can override base class method and variable


darry = Dad()
larry = Son()
harry = Grandson()

# print(darry.guitar)

# electronic device
# pocket gadget
# phone
