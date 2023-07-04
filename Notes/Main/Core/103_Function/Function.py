# a = 9
# b = 8
# c = sum((a, b))
# # built in function

# user defined function
# to make user defined function you have to use def keyword

# syntax:
# def function_name(parameter)

def fun():
    pass
# pass means nothing if we dont do any thing inside block then it will throw an error so we use pass to denote nothing


def function():
    print("you are in the function")


# declaration and the defination of the function
function()
# calling the function


def function1(a, b):
    print("Hello you are in function 1")
    return a + b
    # returnin a+b


v1 = function1(5, 7)
# return the value of a,b and assing in the v
print(v1)
# printing v
