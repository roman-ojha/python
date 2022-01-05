""" 
Iterable: iterable is an object in which __iter__ or __getitem__ method are defined

Iterator: iterator is an object in which __next__ is defined

Iteration: the process of being iterate is called iteration
 """

"""  
Generator: Generator is one kind of a itreator , this is the kind of iterator where we can travers only one time
 """

# for i in range(78):
#     print(i)
# in here 78 number is iterate and generate on the fly or in run time


def gen(n):
    for i in range(n):
        yield i
        # is the generator which will generate on the fly


g = gen(3)
# here now gen is not a function now gen in a generator object
# print(g)
print(g.__next__())
# this will generate the first number
print(g.__next__())
# ths will generate the number 1
print(g.__next__())
# this will give number 2

# print(g.__next__())
# but this will throw an error because this generato is capable of generating from 0-2

h = "harry"
# print(h)

for c in h:
    # string is itrable that's why we itrate stirng one by one
    # it means that because of itrable it contain __iter__ method
    print(c)
# that's why we can itrate it

ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

number = 133214
# here this is an int which in not itrable so if we are trying to itrage it then it will throw an error
