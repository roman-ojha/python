""" 
def print2(str1):
    print2(str1)
    # if we do this the this is the recrsion error because this will call again and again and agian up to infinite
    print("this is ", str1)

print2("Roman") 

"""


# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!

""" itrative approach """


def factorial_iterative(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    # here are uing for loop to do factorial calculation
    return fac


number1 = int(input("Enter then number"))
print("Factorial Using Iterative Method", factorial_iterative(number1))
print(factorial_iterative(number1))

# this metho is the itrative method


"""  Recursion Start """


def factorial_recursive(n):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)


# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 * 3 * factorial_recursive(2)
# 5 * 4 * 3 * 2 * factorial_recursive(1)
# 5 * 4 * 3 * 2 * 1 = 120


number2 = int(input("Enter then number"))
print("Factorial Using Recursive Method")
print(factorial_recursive(number2))

# fabonacci series
# 0 1 1 2 3 5 8 13


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


number = int(input("enter a number to find fibonacci: "))
print(fibonacci(number))
