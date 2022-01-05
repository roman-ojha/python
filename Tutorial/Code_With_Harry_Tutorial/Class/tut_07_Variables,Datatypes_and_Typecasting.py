var1 = "hellow world"  # we can declare string variable like this
var2 = 1  # we can declare int variable like this
var3 = 36.7  # we can declare float variable like this
var4 = " Roman32"
var5 = "50"
var6 = "30"
var7=True
# here python will automatically give type of the variable when we are declaring
print(var1)

print(type(var1))  # it will going to give to type of variable
print(type(var2))
print(type(var3))

print(var2+var3)
print(var1+var4)  # concatenating of two string

# typecasting
print(int(var5)+int(var6))
"""
str()
int()
float()
 """
# if you want to print multiple times

print(5*"Hellow world\n")  # this will print 5 times
print(3*str(int(var5)+int(var6)))

# Take a input from the user
print("Enter your Name= ", end="")
inpname = input()  # when you use input() then it will take a string
print("\nYour name is= ", inpname)

print("Enter any number= ", end="")
inpnum2 = input()
print("\nYour name is= ", int(inpnum2)+10)
# now we can do  this to do mathmatical calculation

# make a calculator to add two number
print("Enter your first number= ", end="")
num1 = input()
print("Enter your second number= ", end="")
num2 = input()
print("the sum of the given number is= ", int(num1)+int(num2))
