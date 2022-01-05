# Q) Write a program to detect whether a number entered by the user is an integer or not.

detect=input("Enter the value to find int or not: ")



if detect.isdigit():
    print("Given value is Intiger")
elif detect.isalpha():
    print("Given value is String")
else:
    print("Given value is nither Int nor String")