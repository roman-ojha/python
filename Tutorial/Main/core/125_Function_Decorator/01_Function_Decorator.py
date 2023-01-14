# EX1: ==================
def num():
    print("Num first function")
    print("Num second function")


num()

# If we want to add another feature inside the 'num' function without adding the statement inside the 'num' function
# in that case we can use decorator
# where Decorator take function as argument and enhance that function and add some new feature into it and return the new function which have the added feature


# Decorator function:
# Function that will enhance the given function
def deco(fun):
    # 'fun' is the function that it take as argument
    def inner():
        print("Inner function before enhancing")

        # calling the passed function into Decorator function
        fun()

        # Added some new feature for 'fun' function
        print("Inner function after enhancing")

    # And also decorator function return the function
    # which we can call as enhanced version of the function that we get
    return inner


# now her we will call the 'deco' function to enhance the 'num' function
result_fun = deco(num)

# Calling the enhanced version of 'num' function
result_fun()
# if you don't want to write these two peace of line in that cause you can use '@' inside the function where we want to add decorator


def deco(fun):
    def inner():
        print("Inner function before enhancing")
        fun()
        print("Inner function after enhancing")
    return inner


# Adding decorator inside the function
@deco
def num():
    print("Num first function")
    print("Num second function")


# now we can just call this 'num' function and it will call the 'deco' function by passing 'num' function as argument
num()


# EX2: ==================
# Decorator function that will modify or enhance the given function
def deco(fun):
    def inner():
        a = fun()
        # here we are getting the value that is returning by the 'fun'
        add = a + 5
        return add

    # now here we are returning the enhanced version
    return inner


@deco
def num():
    # here this function return 10 but when we will use the decorator inside this function we want it to return 15
    return 10


return_val = num()
print(return_val)


# EX3: ==================
# Adding multiple decorator
def deco1(num):
    def inner():
        b = num()
        multi = b * 5
        return multi
    return inner


def deco2(num):
    def inner():
        a = num()
        add = a + 5
        return add
    return inner


def num():
    return 10


# Enhancing by passing num into one decorator function
num = deco1(num)
# Again enhancing by passing num into another decorator function
num = deco2(num)
print("Multi Deco: ", num())
# Multi Deco:  55

num = deco2(deco1(num))
print("Multi Deco: ", num())
# Multi Deco:  280


# Decorator using "@":
@deco2  # Run 2nd
@deco1  # Run 1st
def num():
    return 10


print("Multi Deco: ", num())
# Multi Deco:  55
