"""
Q) Write a recursive function to print the following pattern:
            ****

            ***

            **

            *
"""

def printTraingle(r,c):
    if r == 0:
        return 0
    else:
        if c == 0:
            print("\n")
            return printTraingle(r-1,r-1)
        else:
            print("*",end="")
            return printTraingle(r,c-1)

printTraingle(4,4)


def recurse_triangle(num, char):
    if num > 0:
        recurse_triangle(num-1, char)
        print(char*num,"\n")

recurse_triangle(5, '*')