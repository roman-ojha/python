# extend():
# This method is used to append another list or iterable object at the end of the list
# Syntax: list_name.extend(lst)

a = [10, 20, 30, "Roman", 30]
b = ["Jack", 20.3]

print("A: ", a)
# A:  [10, 20, 30, 'Roman', 30]
print("B: ", b)
# B:  ['Jack', 20.3]

a.extend(b)
print("A: ", a)
# A:  [10, 20, 30, 'Roman', 30, 'Jack', 20.3]
