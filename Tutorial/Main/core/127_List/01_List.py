""" List """
grocery = ["Harpic", "vim bar", "deodrant", "Bhindi", "Lollypop", 56]

# Access all the list elements
print(grocery)

# Access List element
print(grocery[0])
print(grocery[5])

number = [4, 2, 1, 5, 9, 7]
print(number)
print(number[2])

# Accessing with negative indexing
print(number[-1])  # 7
print(number[-2])  # 9
print(number[-3])  # 5
print(number[-4])  # 1

# Modify List:
print("Before: ", number[2], id(number))
# Before:  1 1819450730240
number[2] = 10
print("After: ", number[2], id(number))
# After:  10 1819450730240 # same address

# Empty List
a = []
