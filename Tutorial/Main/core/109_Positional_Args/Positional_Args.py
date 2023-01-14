# Positional Arguments:

# here we are getting two formal argument 'a' & 'b'
# and while calling the function we have to pass the value for 'a' & 'b' in order
def pw(a, b):
    c = a ** b
    print(c)


# first argument value goes to 'a'
# second argument value goes to 'b'
# pw(<a>,<b>)
pw(3, 2)

# we can't also pass more then required argument in the function
# pw(3, 2, 4) # Error
