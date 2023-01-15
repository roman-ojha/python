# slicing on List
# Slicing on list can be used to retrieve a piece of the list that contains a group of elements. Slicing is useful to retrieve a range of elements.
# Syntax: new_list_name = list_name[<start>:<stop>:<step_size>]

a = [10, 20, 30, "Roman", 30, 10, 30]
print(a)
# [10, 20, 30, "Roman", 30, 10, 30]


# From <start> to <stop> position
# a[<start>:<stop>]
print(a[0:5])
# [10, 20, 30, 'Roman', 30]

# From <start> to last position
# a[<start>:]
print(a[1:])
# [20, 30, 'Roman', 30, 10, 30]

# Get/slice last 4 element
print(a[-4:])
# ['Roman', 30, 10, 30]

# From <start> to <stop> by skipping <step_size> every time
# a[<start>:<stop>:<step_size>]
print(a[0:5:2])  # 0 + 2, 2 + 2, 4 + 2,
# [10, 30, 30]

# Get/slice from -3 to -1
# From last 4th element upto [-4-(-1)] = 3 element towards right
print(a[-4:-1])
# ['Roman', 30, 10]

# reverse element
print(a[::-1])
