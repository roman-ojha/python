# + operator on int
sum = 10 + 20
# because int is already defined into python and it knows how to perform '+' operation
# for '+' operator it uses:

# int.__add__(self, other)
sum = int.__add__(10, 20)  # same as 10 + 20
# 10 -> self
# 20 -> other
print(sum)
# These are also called as magic method

# Add to string
str.__add__('a', 'b')  # ab

"""
    *) List of method for overloading:
        a> __add__(self, other) : '+'
        b> __sub__(self, other) : '-'
        c> __mul__(self, other) : '*'
"""

# Operator overloading in user defined types


class A:
    def __init__(self, x):
        self.x = x

    # Defining the __add__ magic method
    def __add__(self, other):
        return self.x + other.x


class B:
    def __init__(self, x):
        self.x = x


a = A(10)
b = B(20)
# Now here we adding 'A' type to 'B' type
sum = a + b  # A.__add__(self, other)
print(sum)

# https://docs.python.org/3/library/operator.html
