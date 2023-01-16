class Employee:
    __info = None
    _password = None

    def __init__(self, password, name):
        self._password = password
        self.name = name

    def _protected_fun(self):
        print("Protected function")

    def __private_fun(self):
        print("Private function")


e = Employee("xyz", "roman")
e._protected_fun()
print(e._password)
