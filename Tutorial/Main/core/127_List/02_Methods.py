number = [4, 2, 1, 5, 9, 7]

print(len(number))
print(max(number))
# this will going to return maximum number
print(min(number))
# this will going to return the munimum number
# you can appened how much you want
number2 = []
number2[1] = 14
# you can change the value of the list like this
print(number2)

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
