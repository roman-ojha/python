# Q) What will be the result of the following expression:  float a = 7/4 * 9/2

expression="7/4*9/2"
a=float(int(expression[0])/int(expression[2]))*float(int(expression[4])/int(expression[6]))

print("The result of the expression: ",expression,"is:",a)