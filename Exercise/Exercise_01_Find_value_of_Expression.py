# Q) Find the value of the given expression:

# 2^3*10^2/2
import operator

print("Enter the epxression to find the result:\nEX: 2^3*5^6/10\n")
print("Operator Allowed:\na) Multiplication(*)\nb) Devision(/)\nc) Addition(+)\nd) Subtraction(-)\ne) Power(^)")

expression=input("Expression: ")

def isOperator(expression):
    switch={
        "/":True,
        "*":True,
        "+":True,
        "-":True,
        "^":True,
    }
    return switch.get(expression,False)



concatDigit=""
for i in range(0,len(expression)):
    result=float
    if expression[i].isdigit():
        print("Digit",expression[i])
        concatDigit=concatDigit+expression[i]
    elif isOperator(expression[i]):
        print("Operator",expression[i])
        concatDigit=""
    else:
        print("Invalid Expression, Plese Try Again!!!")
        break
