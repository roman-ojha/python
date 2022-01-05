# Lambda functions or anonymous functions

# general function
# def add(a, b):
#     return a+b

"""  lambda function """
# we can use labda function like this which operate same as the normal function but have the small line of code
# --------------------------------------
# making a minus function in general way:


def minus1(x, y):
    return x-y


print(minus1(9, 4))
# ----------------------------------------------
# making a minus function in lambda function way:
# syntax: lambda parameter_list: expression


# minus2 = lambda x,y: x-y
# print(minus2(9, 4))

# ---------------------------------------------
# again general function:


def fun1(a1):
    return a1[1]


a1 = [[1, 14], [5, 6], [8, 23]]
a1.sort(key=fun1)
# key is an argument which takes function as an input and function need to return element
"""
here we return a1[1] so this will return second element and sort them so second element are 14,6,23 and after sorting them it become 6,14,23 that way if we print a1 we get after sort [[5, 6], [1, 14], [8, 23]] 
if we return a1[0] then it will return first elemet and sort them in accending order and if we will print it, it will give :
[[1, 14], [5, 6], [8, 23]]

"""
# we can explore sort function and the key argument
print(a1)
# ----------------------------------------------
#  now using lambda function


a2 = [[1, 14], [5, 6], [8, 23]]
a2.sort(key=lambda x: x[1])
print(a2)
# --------------------------------
