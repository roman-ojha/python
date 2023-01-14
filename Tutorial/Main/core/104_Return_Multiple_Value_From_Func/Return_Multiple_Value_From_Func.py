# Return Multiple value from function

def add_sub(a, b):
    add = a + b
    sub = a - b

    return add, sub
    # return (add, sub)


add, sub = add_sub(10, 3)
print(add)
print(sub)


def add_sub(a, b):
    add = a + b
    sub = a - b

    return add, sub, 5
    # return (add, sub)


add, sub, num = add_sub(10, 3)
print(add)
print(sub)
print(num)
