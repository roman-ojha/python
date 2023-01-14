def function_name_print(a, b, c, d):
    print(a, b, c, d)


function_name_print("harry", "Rohan", "Skillf", "Hammad")
# by this function we have to define and put that that much argument we in at the initial
# but if i want to add another name in the argument then that will be error because function only have four argument so, if we want to add a lots of name after then it is not the write way to do

""" *args """


def funarg(normal, *args):
    # in here in *args parameter comes as an tuple
    # this is not compolsory to put args as a name
    # we can put a normal argument as well
    # you have to put normal argument in start and then *args
    # print(type(args))
    # print(args[0])
    print(normal)
    for items in args:
        print(items)


har = ["harry", "Rohan", "Skillf", "Hammad", "shivam"]
normal = "Roman"
funarg(normal, *har)
# funarg(normal) # this will also ok

# now  in this case we made a list and send that list as an argument in the funarg function now  can update ,delete do any things that you want because now we can get any argument in the function after update as well

""" **kwargs """


def funarg2(normal, *args, **kwargs):
    # order of the argument is (normal argument, *args argument, *kwargs)
    print(normal)

    for items in args:
        print(items)
    print("\nNow i would like to introduce some of our heros:")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


har2 = ["harry", "Rohan", "Skillf", "Hammad", "shivam"]
normal2 = "Roman"
kw = {
    "Rohan": "Monitor",
    "harry": "Fitness Instructor",
    "The Programmer": "Coordinator",
    "Shivam": "cook"
}
funarg2(normal2, *har2, **kw)
