""" List """
grocery = ["Harpic", "vim bar", "deodrant", "Bhindi", "Lollypop", 56]
print(grocery)
# this will going to print the list of grocery
print(grocery[0])
print(grocery[5])
number = [4, 2, 1, 5, 9, 7]
print(number)
print(number[2])
number.sort()
# this will going to make number in accending order
number.reverse()
# now this will going to reverse the number
print(number)
print(number[0:5])
# you can slice the list as well like this
print(number[0:6:2])
# this will also escapeing 1,1 list number form list
print(number[::-1])
# in slicing list you only have to take -1 you dont have to take above form that
print(len(number))
print(max(number))
# this will going to return maximum number
print(min(number))
# this will going to return the munimum number
number.append(16)
print(number)
# this will going to add 16 at the end of the list
number.append(16)
number.append(16)
print(number)
# you can appened how much you want
number2 = []
number2.append(13)
number2.append(24)
number2.append(6)
print(number2)
# we can make a list like this as well
number2.insert(1, 4)
# first argument is index , where you want to insert and another argument is which value you want to insert
number2.remove(24)
# this will going to remove
number2.pop()
# this will going to remove the last index of the list
number2[1] = 14
# you can change the value of the list like this
print(number2)
""" 
Mutable -> can change 
Immutable -> cannot change

here list are mutable and Tuples is Immutable
the value in the tuples are not changeable
 """

tp = (1, 2, 3)
# this is how we can declare tuple
# tp[1] = 8
# we had alrady say that we can't change the value of the tuple
tp1 = (1,)
# if we want to make tuple of one value then also we have to put "," to say that it is a tuple
print(tp)

a = 1
b = 5
temp = a
a = b
b = temp
print(a, b)
# this is the traditional way to swap two thing but in python we can do this:
a, b = b, a
print(a, b)
