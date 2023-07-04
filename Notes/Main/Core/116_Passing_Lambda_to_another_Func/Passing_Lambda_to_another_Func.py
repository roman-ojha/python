# We can pass lambda function to another function


# defining the normal function
def show(a):
    # calling the lambda function that we get as parameter
    value = a(8)
    print(value)


# passing lambda function to 'show' function
show(lambda x: x)
