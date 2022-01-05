""" 
pattern printing
input=integer n
boolean =True of False

if True:
*
**
***
****

if False
****
***
**
*

 """

print("Enter the number of rows that you want to print: ", end="")
n = input()
i = 0
j = 0

while(True):
    print("Enter 0 or 1: ", end="")
    boolean1 = input()
    if boolean1 == "1":
        print("True ")
        while(i < int(n)):
            j = 0
            while(j <= i):
                print("*", end="")
                j = j+1
            print("\n")
            i = i+1
        break
    elif boolean1 == "0":
        print("False ")
        i = int(n)
        while(i > 0):
            j = i
            while(j > 0):
                print("*", end="")
                j = j-1
            print("\n")
            i = i-1
        break
    else:
        print("Invalid number!! Enter 0 or 1")

        continue
