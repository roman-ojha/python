# Q) Write a program to print the multiplication table of a given number n.

n=int(input("Enter the number to get the multiplication:"))

for i in range(0,11):
    print(n,"* ",i,"=",n*i)
