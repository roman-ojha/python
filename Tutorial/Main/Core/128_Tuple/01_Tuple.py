tp = (1, 2, 3)
# this is how we can declare tuple
# tp[1] = 8
# we had alrady say that we can't change the value of the tuple
tp1 = (1,)
# if we want to make tuple of one value then also we have to put "," to say that it is a tuple
print(tp)

a = 1
b = 5
temp = a
a = b
b = temp
print(a, b)
# this is the traditional way to swap two thing but in python we can do this:
a, b = b, a
print(a, b)
