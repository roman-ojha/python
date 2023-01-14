def function2(a, b):
    """This is a function which will calculate average of two numbers
    this function doesnt work for three numbers"""
    # if you put the content inside it """ """  in the function then it will called as a docstring
    # in a function string written in the first line is called as docstring
    average = (a + b) / 2
    # print(average)
    return average


v = function2(5, 7)
print(v)
print(function2.__doc__)
# we are accessing docstring using this syntax
