# pop()
# This method will used to remove last element from the existing list

a = [10, 20, 30, "Roman"]
print(a)
# [10, 20, 30, 'Roman']

a.pop()
# this will going to remove the last index of the list
print(a)
# [10, 20, 30]

# pop(n)
# This method is used to remove an element specified by position number, from the existing list and returns removed element
# Syntax: list_name.pop(<position_number>)
a.pop(1)
print(a)
# [10, 30]

# it also return the popped element
elm = a.pop(0)
print("Popped element: ", elm)
# Popped element:  10
