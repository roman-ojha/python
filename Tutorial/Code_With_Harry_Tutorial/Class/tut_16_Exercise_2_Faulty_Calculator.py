# question:
# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

# solition:

print("Calculator:")
print("Enter the operator form which you want to perform the calculation: ", end="")
operator = input()
print("Enter first number: ", end="")
num1 = input()
print("Enter second number: ", end="")
num2 = input()
res = 0
if num1 == "45" and num2 == "3" and operator == "*":
    print("your Result is: 555")
elif num1 == "56" and num2 == "9" and operator == "+":
    print("your Result is: 77")
elif num1 == "56" and num2 == "6" and operator == "/":
    print("your Result is: 4")
elif operator == "/":
    res = int(num1) / int(num2)
    print("your Result is: ", res)
elif operator == "*":
    res = int(num1)*int(num2)
    print("your Result is: ", res)
elif operator == "+":
    res = int(num1)+int(num2)
    print("your Result is: ", res)
elif operator == "-":
    res = int(num1)-int(num2)
    print("your Result is: ", res)
else:
    print("invalid number! please Enter the correct number or operator ")
