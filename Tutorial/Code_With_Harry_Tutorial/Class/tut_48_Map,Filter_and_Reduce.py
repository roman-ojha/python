""" --------------------------MAP------------------------------ """
# numbers = ["3", "34", "64"]

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# -> we are changing list stirng of number into form of int and after that we can do calculation
# -> but this can be done in just one line by using map

# numbers = list(map(int, numbers))
# -> in here map(function which has to apply in all element of the list,list name)
# -> here maps return object as a default so we have to change it into list

# numbers[2] = numbers[2] + 1
# print(numbers[2])

# -------------------------------
# def sq(a):
#     return a*a
#
# num = [2,3,5,6,76,3,3,2]
# square = list(map(sq, num))
# -> in here we pass function as a first argument in map which perform some task and return something
# print(square)
# ---------------------------
# num = [2,3,5,6,76,3,3,2]
# square = list(map(lambda x: x*x, num))
# -> here we can use lambda function as well
# print(square)

# ----------------------------
def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square, cube]
# -> we are giving function name as list name in func list
for i in range(5):      
    # -> in here we are giving range to perform for loop upto  that range
    val = list(map(lambda x:x(i), func))
    print(val)
# -> and in here we are uing a lambda function which will return function and i as an argument so, after that function from that list will call and ger "i" as an argument and perform the task and return the value from the function and after ther we get the return value as an object because of using map so we have to convert it into list and print that list
# ------------------------------------------------------------------------

""" --------------------------FILTER------------------------------ """
# list_1 = [1,2,3,4,5,6,7,8,9]
#
# def is_greater_5(num):
#     return num>5
# -> here if num is greater then 5 then it will return true other wise it will return false
#
# gr_than_5 = list(filter(is_greater_5, list_1))
# -> filter will also return object so we have to convert it into list so we use list function
# -> filter(first is function name , another is iterable)
# print(gr_than_5)
# -> so after giving num>5 there will only print number greater then 5
""" --------------------------REDUCE------------------------------ """
from functools import reduce
list2 = [1, 2, 3, 4, 5]

num = 0
for i in list2:
    num = num+i
print(num)
# this is also the way to reduce the list or we can say that to sum,multiplication or do calculation of list but we can do that by using reduce in effecient way

# redece is the part of the fnctools module
# here functools is the module of the python and reduce is the function of that functools module
list1 = [1, 2, 3, 4, 2]
num = reduce(lambda x, y: x*y, list1)
# reduce(it also take first argument as function, and another is list or say data )
# in here redece function work like this:
# first -> x*y = 1*2 = 2
# second -> x*y(2*y) = 2*3 = 6
# third -> x*y(6*y) = 6*4 = 24
# fourth -> x*y(24*y) = 24*2 =48

print(num)
