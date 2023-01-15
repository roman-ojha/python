import tut_45_How_Import_Works_In_Python_2 
# NOTE: previously it work like this but now i have to do this:

# to import the spacific variable or function
from .tut_45_How_Import_Works_In_Python_2 import variable1

# here we can insert our own project by importing using file name
# now we can connect both file and if we make a variable and function in another file then we can use that variable and function in the project easily
import flask as fl
# where this flask module is come in the program how we import it from where we import these kind of module ,to get this kind of the infomation we have one  module:
import sys
# print(fl.__version__)
# you can get the version of the module
print(sys.path)

var = tut_45_How_Import_Works_In_Python_2.variable1
# we are importing variable from the another project
print(var)
print(tut_45_How_Import_Works_In_Python_2.function(1, 2))
# this is the function of the another python file and which takes an two argument and return sum

# another way to directly access variable and function is:
""" 
from tut_45_How_Import_Works_In_Python_2 import variable1 

print(variable1)
# now here we are directly access variable1 without using name of the module
# but this is not recomended for the beginners it might cause ambiguty error
"""
""" 
NOTE: when you are importing modules them import will going to search that module in the local directory or path and if that local directory doesnot have that module then it will go to the another sequence of path that python automatically search  
NOTE: the sequence of path that what path import is searching in sequence that we can find by using 
import sys and print that sys.path which we had did before

NOTE: that's why we dont have to make the python file name as the name of the default module and external module
 """