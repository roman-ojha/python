import random
# random is the module of the python we can search the function or documentation of modules in internet
# we can go to the internet and search for the mocule and read which mocule will do what
random_number = random.randint(0, 5)
# random.randint is the function of the random module which will return random number or generate random number
print(random_number)

rand = random.random() * 100
# here ramdom.random() will generate random number from o-1  and if we want to return random number from 0-100 then we have to multiply by 100
# thses are not intiger these are numbers
print(rand)


lst = ["Star Plus", "DD1", "Aaj Tak", "CodeWithHarry"]
choice = random.choice(lst)
# this will also return random choice from the given data
print(choice)

# we can install modules form the tarminal by using:
""" 
    pip install module_name
"""
