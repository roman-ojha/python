a = [10, 20, 30, "Roman"]
print(a)
# [10, 20, 30, 'Roman']

# insert method will insert the new element by in between, beginning, end of the list
# and it will shift other element accordingly
a.insert(1, 4)
print(a)
# [10, 4, 20, 30, 'Roman']

a.insert(3, "Jack")
print(a)
# [10, 4, 20, 'Jack', 30, 'Roman']
