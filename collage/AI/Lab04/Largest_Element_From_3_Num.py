a = int(input("Enter First Number A: "))
b = int(input("Enter Second Number B: "))
c = int(input("Enter Third Number C: "))

if(a > b):
    if(a > c):
        print("A is Greatest Element")
    else:
        print("C is Greatest Element")
else:
    if(b > c):
        print("B is Greatest Element")
    else:
        print("C is greatest element")
