# Passing array to function
from array import *


def show(ar):
    print(ar)
    print(type(ar))
    for i in ar:
        print(i)

    return ar


# Creating int type of array
a = array('i', [101, 102, 103, 104])
ar = show(a)

print(ar)
print(type(ar))
for i in ar:
    print(i)
