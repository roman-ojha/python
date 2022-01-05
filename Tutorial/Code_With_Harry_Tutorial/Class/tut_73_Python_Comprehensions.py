ls = []

for i in range(100):
    if i % 3 is 0:
        ls.append(i)

print(ls)

# this is the long process we can do this in short form or short process

lis = [i for i in range(100) if i % 3 == 0]
print(lis)
# this will also give the same output
# this is called as list comprehensions

# we also have dictionary comprehension and set comprehensions and generator comprehensions

# dis={0:"item0", 1:"item1" ......... upto 1000}
# if we want to do this upto 1000 then it will take a lot of time
# so we have dictionary comprehensions

dic1 = {i: f"item{i}" for i in range(2, 20) if i % 3 == 0}
print(dic1)
# this is also the way to do by dictonary comprehensions

# if we want to reverse the dictionary then also we can use the dictionary comprehensions
dic2 = {value: key for key, value in dic1.items()}
print(dic2)


""" set comprehensions """
dresses = {dress for dress in {"dress1", "dress2",
                               "dress1", "dress2", "dress1", "dress2", }}
print(dresses)


""" generator comprehensions """

evens = (i for i in range(10) if i % 2 == 0)

print(evens.__next__())
print(evens.__next__())

# so we had alrady sa that generator can only be able to itrate one time an we had alrady itrate two times now it will itrate after two times
for i in evens:
    print(i)
