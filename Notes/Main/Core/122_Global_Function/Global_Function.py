# Global Function:
# This function return a table of current global variables in the form of dictionary.


# global variables
a = 50


def show():
    a = 10
    # if you want to access the global variable 'a' & as well local variable 'a' in that case we have globals()

    x = globals()['a']
    # globals()['<name_of_the_global_variable>']

    # if we will modify the 'x' variable it will not reflect to the global variable
    x = 40

    print(a)
    print(x)


show()
print(a)
