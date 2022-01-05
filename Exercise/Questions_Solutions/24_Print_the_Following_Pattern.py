"""
Q) Write a program using functions to print the following pattern:
            *

            **

            ***

            ****
"""

for i in range(0,4):
    for j in range(0,i+1):
        print("*",end="")
    print("\n")