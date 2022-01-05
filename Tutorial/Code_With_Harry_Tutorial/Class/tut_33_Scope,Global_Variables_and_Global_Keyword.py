l = 10
g = 20
# this is the global variable
# and this variable can be access by any function of inside the block


def function1(n):
    l = 5
    # this is the local variable where we and this variable value can be access or have the scope only upto the end of this function block
    print(l)
    # here the value of l will be 5 because we have defined the value of l inside the block if we did't define the value of l inside the block then the value will be 10 because in the global variable we have the value of the l
    print(n, "I have Printed")
    # in the block we can access the global variable but cant change the value of the global variable
    # if we want to access and want to change at the block then the we have to use the global keyword
    global g
    # now we get the permition to chage the value of g
    g = g + 50
    print(g)


function1("this is me")
print(l)
# here the value of the l will print 10 because the statemet  is not ate the block section and l value is define  at  the global scope
print(g)
# here we set global variable g value 20 but get the value 70 because we have changed the value at the function block by using the global keyword


def harry():
    x = 20

    def rohan():
        global x
        x = 88
        # here we cant change the global variable because we did not define the global variable x in gloval section and inside function defining the variable is not calling as the global variable
        # if the global section will not have the variable called as x then it will make variable named as x and assign the value 88 in that variable now x is the global variable
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)


harry()
# here we get the value 20 because rohan function did not change the value to 88
print(x)
# if we do this then x value will print 88 because global variable will made by the global keyword automatically
