# def function1():
#     print("Subscribe now")
#
# func2 = function1
# -> we are assigining another function to the new function and call the func2 funciton
# del function1
# -> this will delete the function1() but we have alrady assign function1() as func2() so we had alrady make the copy of function1()
# func2()

# def funcret(num):
#     if num==0:
#         return print # -> we are returning print function
#     if num==1:
#         return sum # -> here we are returning sum function
#
# a = funcret(1)
# here this show that we can return function by using function to retun them
# print(a)

# def executor(func):
#     func("this")
#
#
# executor(print)
# here we pass the print function and we are using print function inside the function by passing print function as an argumment


""" -----------------Decorators------------------------ """

"""
Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it. 
"""

"""
Properties of first class functions:

A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …
"""

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec


# here we are passing who_is_harry function as an argument for function dec1 by using @ dec and assign that dec1 function to the who_is_harry() function
@dec1
def who_is_harry():
    print("Harry is a good boy")

# who_is_harry = dec1(who_is_harry)
# -> thsi is same as doing @dec1 but @dec1 need to be at previous line of  the function that we want to pass as an argument in dec1()
who_is_harry()

""" 
NOTE: 
1)  we can pass function as an argument  
2)  we can return function as well and 
3)  we can assign one function to another function 
 """


def div(a,b):
    return a/b

def smart_div(func):
    def inner_func(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner_func


@smart_div
def div2(a,b):
    return a/b

div1 =smart_div(div)


print(div2(2,4))
print(div1(2,4))
