# Q) Write a program to sum first n even numbers using a while loop.

n=int(input("enter the n even number to find the sum: "))
i=0
sum=0
while i<n:
    sum=sum+2*i
    i+=1

print("The sum of the first n even number is: ",sum)
