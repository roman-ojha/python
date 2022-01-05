# Q) Use comparison operators to find out whether a given number is greater than the user entered number or not.

a=int(input("Enter number A: "))
b=int(input("Enter the B: "))

if a>b:
    print("A is greater then B")
elif a<b:
    print("B is greater then A")
elif a is b:
    print("A=B")
else:
    print("Invalid number")