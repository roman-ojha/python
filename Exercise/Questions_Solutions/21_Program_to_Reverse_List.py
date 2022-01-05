# Q) Write a program to reverse an array.

ArrList=[1,2,3,4,5,6,7,8,9,10]

print("Array before reverse: ")
for item in ArrList:
    print(item,end=" ")

print("Array after reverse:")
j=len(ArrList)-1
for i in range(0,int(len(ArrList)/2)):
    ArrList[i],ArrList[j]=ArrList[j],ArrList[i]
    j-=1


for item in ArrList:
    print(item,end=" ")