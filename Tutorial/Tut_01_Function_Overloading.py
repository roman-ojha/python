class Number:
    def __init__(self, required_param, optional_param1 = None, optional_param2 = None):
        # here we are assgning default value as None because of that it can be able to use as Constructor overloading
        self.required_param = required_param
        self.optional_param1 = optional_param1
        self.optional_param2 = optional_param2

obj1=Number(1)
obj1=Number(1,2)
obj1=Number(1,2,3)