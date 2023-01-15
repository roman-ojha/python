# Global keyword

# Global variable:
a = 50


def show():
    # Local variable
    a = 10

    # if we will try to access 'a' then we can only access local variable
    print(a)
    # 10


show()

# but here we can access global variable here
print(a)
# 50


def show():
    # So if we will try to access the global variable for assign to the same name variable
    # this will throw an error
    # to be able to access the global variable here we can use global keyword
    global a
    a = a + 1
    # now the value that we change for 'a' will for for global variable
    print(a)
    # 51


show()
print(a)
# 51
