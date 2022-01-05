# Q) Write a Java program to find whether an array is sorted or not.

arrList=[1,2,3,4,5,6,7,8,9,10]

count=1
previtem=arrList[0]
for i in range(1,len(arrList)):
    if arrList[i]>=previtem:
        count+=1
    previtem=arrList[i]

if count is len(arrList):
    print("The given array is sorted")
else:
    print("the given array is not sorted")