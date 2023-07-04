# EX1: ===========
def val(x):
    # here we get the x as object reference
    print(x, id(x))
    # 10 2471032914448

    # creating new x object
    # Because integer object are immutable(not modifiable)
    x = 15
    print(x, id(x))
    # 15 2471032914608


# Creating x object
x = 10
val(x)
print(x, id(x))
# 10 2471032914448


# EX2: ======
def val(lst):
    # getting 'lst' list as reference
    # and also it will not create a new object 'lst' and will not allocated the memory inside stack

    print("Inside function before append: ", lst, id(lst))
    # Inside function before append:  [1, 2, 3] 2339602429824

    lst.append(4)
    # appending the new value into the 'lst'
    # we are appending this value to the global 'lst' because here we are referencing to the global 'lst'
    # because list object are mutable(modifiable)

    print("Inside function after append: ", lst, id(lst))
    # Inside function after append:  [1, 2, 3, 4] 2339602429824


# Creating list object
lst = [1, 2, 3]
print("Before calling function: ", lst, id(lst))
# Before calling function:  [1, 2, 3] 2339602429824
val(lst)
print("After calling function: ", lst, id(lst))
# After calling function:  [1, 2, 3, 4] 2339602429824


# EX3: ======
def val(lst):
    print("Inside function before append: ", lst, id(lst))
    # Inside function before append:  [1, 2, 3] 1783499777280

    # Now here we are  Creating a new object
    lst = [5, 6, 7]

    print("Inside function after append: ", lst, id(lst))
    # Inside function after append:  [5, 6, 7] 1783499782208


# Creating list object
lst = [1, 2, 3]
print("Before calling function: ", lst, id(lst))
# Before calling function:  [1, 2, 3] 1783499777280
val(lst)
print("After calling function: ", lst, id(lst))
# After calling function:  [1, 2, 3] 1783499777280
