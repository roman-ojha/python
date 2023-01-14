# Default Arguments

def show(name, age=27):
    print(f"Name: {name} Age: {age}")


# Calling function without passing default argument
show("Roman")

# Calling function with passing default argument
# and it will replace the default argument value
show("Jack", 31)

# Default argument with keyword argument
show(name="Harry")
show(name="Harry", age=33)
