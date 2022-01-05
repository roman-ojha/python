# Q) Write a program to find the factorial of a given number using for loops.

n=int(input("Enter the value to find the factorial:"))

factorial=1
for i in range(1,n+1):
    factorial=factorial*i

print("Factorial of the given number is:",factorial)