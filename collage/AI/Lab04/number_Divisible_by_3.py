def fun(variable):
    if variable % 3 == 0:
        return True
    else:
        return False


sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

requiredNum = filter(fun, sequence)
print("The Number Divisible by 3 from 0-10 is: ")
for num in requiredNum:
    print(num)
