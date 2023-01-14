def add():
    y = 20
    return (lambda x: x + y)


lambda_add = add()
value = lambda_add(2)
print(value)
