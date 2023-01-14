# Keyword variable length argument:

def add(**num):
    # num is a dictionary
    z = num['a'] + num['b'] + num['c']
    print(z)


add(a=3, b=4, c=5)


def add(x, **num):
    z = x + num['a'] + num['b'] + num['c']
    print(z)


add(2, a=3, b=4, c=5)
