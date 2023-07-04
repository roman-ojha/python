class Duck:
    def walk(self):
        print("thapak thapak")


class Horse:
    # both the class have same method name with different print
    def walk(self):
        print("tabdak tabdak")


class Cat:
    def talk(self):
        print("myau myau")


def my_function(obj):
    # here we can see that we are getting an object type
    # after that we are calling the walk function
    # this function don't know which object we are getting
    # and which object walk() method we are calling
    # So python doesn't care what you pass as 'obj' it only care that that 'obj' should have '.walk()' function then it will work
    obj.walk()


d = Duck()
h = Horse()
c = Cat()

# passing 'Duck' object type into the function
my_function(d)

# passing 'Horse' object type into the function
my_function(h)


# But we know that 'Cat' class doesn't have the 'walk' method, so if we will pass 'Cat' type of object to this function the it will throw an error
# And it is an run time error
# my_function(c)


a = 10
# a doesn't not have it's own type because we are passing '10' as int, right now 'a' is of type int

a = 'Roman'
# so here 'Roman' is of type string and we are reassigning it to 'a' it means that now 'a' is of type String
