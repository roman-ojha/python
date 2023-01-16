# In python we can't define the same name function with different parameter
# Rather we have to perform different task with the same function/method
class MyClass:
    # For that we can given default argument value in each parameter
    # Now we can call with any number of argument while calling this method
    # sum()
    # sum(10)
    # sum(10,20)
    # sum(10,20,30)
    def sum(self, a=None, b=None, c=None):
        # now we can perform the task according to the number of argument that we get

        # if a != None and b != None and c != None:
        if a and b and c:
            s = a + b + c
            return s
        elif a and b:
            s = a + b
            return s
        elif a:
            return a
        return 0


obj = MyClass()
sum = obj.sum(10, 20, 30)
print(sum)
sum = obj.sum(10, 20)
print(sum)
sum = obj.sum(10)
print(sum)
sum = obj.sum()
print(sum)
