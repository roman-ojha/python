# Q) Write a program to find out whether a given integer is present in an List or not.

integer=int(input("Enter the integer to check wheter the given number is in list of not:"))

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

    