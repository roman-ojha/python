# Dictionary is nothing but key value pairs
d1 = {}
# you can make blank dictionary like this
# print(type(d1))
d2 = {"Harry": "Burger",
      "Rohan": "Fish",
      "SkillF": "Roti",
      "Shubham": {"B": "maggie", "L": "roti", "D": "Chicken"}}
# the value of the dictionary can be any thing like list ,dictionary , tuples
# note that keys needs to be immutable types

# d2["Ankit"] = "Junk Food"
# we can insert keys value in the dictionary

# d2[420] = "Kebabs"
# can do this for a key to make a number

# print(d2)
# printing dictionary

# del d2[420]
# deleting dictionary keys and value

# print(d2["Shubham"])
print(d2["Shubham"]["B"])
# you can access dictionary inside dictionary

# d3=d2
# here this will not going to make or assign to the another variable 
# if we will change the dictionary of d3 then the dictionary of d2 will also change
# so that we have to use copy() function

# d3 = d2.copy()
# we can copy dictionary as well and assign that doctonary to the another dictionary
# del d3["Harry"]
# but if we delete d3 dictionary keys and values then the d2 dictionary kays and values will also delete because d3 is a pointer who point d2 dictionary and d2 is also the pointer who pointer d2 itself so , by using copy new dictonary will not form it just refrence the main dictionary where it is copy from

print(d2.get("Harry"))
# we can excess dictionary by get function as well

# d2.update({"Leena":"Toffee"})
# we can update the dictionary and put another keys and values in the dictionary
# print(d2.keys())
# keys function will going to give the keys of the dictionary
print(d2.items())
# items function will going to give the keys value pear
