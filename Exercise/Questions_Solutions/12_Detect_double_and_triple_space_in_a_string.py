#Q) Write a program to detect double and triple spaces in a string.

string=input("Enter the string to detect double or triple space in the string:\n")

countSpace=0
countdouble=0
countTriple=0
for i in range(0,len(string)):
    if string[i].isalpha():
        if countSpace is 2:
            countdouble+=1
        elif countSpace is 3:
            countTriple+=1
        countSpace=0
    if string[i] is " ":
        countSpace+=1

print("double space are:",countdouble)
print("triple space are:",countTriple)