class Duck:
    def walk(self):
        print("thapak thapak")


class Horse:
    def walk(self):
        print("tabdak tabdak")


class Cat:
    def talk(self):
        print("myau myau")


def my_function(obj):
    # we can check does the object 'obj' that we are getting have the invoked method or not
    if hasattr(obj, 'walk'):
        # if 'obj' have 'walk' method only at that type we want to run it's method
        obj.walk()
    # else:
    #     print(obj.__class__.__name__, "Object Doesn't have walk method")

    # Or:
    if hasattr(obj, 'talk'):
        obj.talk()


d = Duck()
h = Horse()
c = Cat()

my_function(d)

my_function(h)

my_function(c)
