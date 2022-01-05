# 01) Write a program to print the following pattern :
        # ****
        # ***
        # **
        # *

for i in range(0,4):
    for j in range(4,i,-1):
        print("*",end="")
    print("\n")

