# list1 = [ ["Harry", 1], ["Larry", 2],
#           ["Carry", 6], ["Marie", 250]]
# dict1 = dict(list1)
# it will going to make a dictonary and assing it to the dict1

# for item in dict1:
#     print(item)
# for item, lollypop in dict1.items():
#     print(item, "and lolly is ", lollypop)
# here 'item' will give the first value in here name and lollypop will give second value in here number
#  here items() function is used to print the items of the dict1

items = [int, float, "HaERRY", 5, 3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item >= 6:
        print(item)


integer=5
# Item and value in list
intList=[1,2,3,4,5,6,7,8,9,10]
count=1
for index,value in enumerate(intList):
    if integer is value:
        print("The given integer is in the index",index)
        break
    elif count is len(intList):
        print("The given integer is not in the list")
    else:
        count+=1


# incremental for loop
for i in range(0,10,2):
    # range(start index, stop index, step)
    print(i)

# decremental for loop
for i in range(10,0,-1):
    print(i)