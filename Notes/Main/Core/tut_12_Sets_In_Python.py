# set contain the unique value
s = set()
# we can make the sets like this
# print(type(s))

# l = [1, 2, 3, 4]
# s_from_list = set(l)
# we can make the list as a set in python
# s_from_list = set([1, 2, 3, 4])
# we can do this as well to make a set
# print(s_from_list)
# print(type(s_from_list))

s.add(1)
s.add(2)
# add function will add or insert the value in the given set
# s.add(1)
# if we want to add the same value to the set then we can't be able to do that because set contain the unique value that means we cant append the same value in the same sets
s1 = s.union({3})
# union function will make the union of the set and store the given value in the set
# in this setutaion we are assigining s to the s1 by doing union and we are giving the value 3 in the union function it means that s1 is a set which contain the value 1,2,3 because we have alrady define the value 1,2 so, it will make a union and store that value to the s1
print(s, s1)
s2 = s.intersection({1, 2, 3})
print(s2)
# intersection function will intersect the value and return the set contain same value
print(len(s))
print(min(s))
# it will return the minimum value at the set
print(max(s))
# it will return the maximum value at the set
"""  other function are :
1) difference 
2) symmetric_difference
3) isdisjoint
"""
# s.remove(2)
# if will remove the value from the set

# s1 = {4, 6}
# print(s.isdisjoint(s1))
