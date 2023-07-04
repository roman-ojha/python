# you can add one string to the another variable
import math

me = "Roman"
a = "this is %s" % me
print(a)
# this concept or way is confusing if you are manipulating big string

me2 = "harry"
n1 = 13
a = "this is %s and number is %s" % (me2, n1)
print(a)
# we are passing tuple in here

# so there is the another way to do as well
me3 = "harry"
n2 = 13
# a = "This is {} and number is {}"
# you can do this as well and pass the varialbe in {} sequenclly
# but you can do this as well
a = "this is {1} and number is{0}"
# now in here sequence had change now n2 will print at the first because me3 is at 0 and n2 is at  1 in format() function
b = a.format(me3, n2)
print(b)
# this is also  the way to do but in here also the readability is massup

""" F-Strings """
# F-strings full form is Fast-string
# to make f-string:
me4 = "john"
n3 = 13
a = f"This is {me4} and the number is {n3} and {4*6} and {9/3} and {math.cos(65)}"
# in f string we can use functio and the function from module
print(a)
# writing f before stirng called as f string
