# Q) Write a program to find the maximum,minimum element in an List.

arrList=[54,23,76,12,43,87,100,43,76,89,143]
max=arrList[0]
min=arrList[0]

for i in range(0,len(arrList)):
    if arrList[i]>max:
        max=arrList[i]
    if min>arrList[i]:
        min=arrList[i]

print("Maximum:",max)
print("Minimum:",min)