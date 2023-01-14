# for get_x lambda we have added the default argument value for 'x'
get_x = lambda x=10: (lambda y: x + y)

# get_x() call "lambda x=10:()" and return the lambda function
add = get_x()
# here 'add' is the lambda function that is return by the 'get_x' lambda function

# because 'add' is also a lambda function we have to call to return the value
print(add(3))

# Or we can just use one expression to call the nested lambda function
print(get_x()(3))
