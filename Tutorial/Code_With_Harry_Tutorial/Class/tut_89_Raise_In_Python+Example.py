
a = input("What is your name")
# b = input("How much do you earn")

# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
# this is the zerodivisionerr , here we are sayin that if "b" will be zero then we are stoping the program here
# we can search built in exception in internet

# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
# we are raising the exception that if this imput will have number then that is not allowed
# we are stoping the program if some error is happinning

# print(f"Hello {a}")


# Task - Write about 2 built in exception


c = input("Enter your name")
try:
    print(a)

except Exception as e:

    if c == "harry":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exception handled")
