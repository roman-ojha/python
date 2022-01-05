# Q) Write a program to calculate the sum of the numbers occurring in the multiplication table of 8.


sum=0
for i in range(0,11):
    sum=sum+8*i

print("The sum is:",sum)