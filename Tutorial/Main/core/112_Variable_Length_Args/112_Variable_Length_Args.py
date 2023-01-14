# Variable length arguments:

def add(*num):
    # num is a tuple
    z = num[0] + num[1] + num[2]
    print(z)


add(5, 4, 3)


def sum(x, *num):
    z = x + num[0] + num[1]
    print(z)


sum(5, 4, 3)
