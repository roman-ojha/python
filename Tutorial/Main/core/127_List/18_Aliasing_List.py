# Aliasing list:
# Aliasing means giving another name to the existing object. it doesn't means copying.

a = [10, 20, 30, 40, 50]

# Aliasing  list 'a' and creating new name 'b' as well
b = a
print("A: ", a)
print("B: ", b)
# A:  [10, 20, 30, 40, 50]
# B:  [10, 20, 30, 40, 50]

print("Modifying A")
a[1] = 55
print("A: ", a)
print("B: ", b)
# Modifying A
# A:  [10, 55, 30, 40, 50]
# B:  [10, 55, 30, 40, 50]

print("Modifying B")
b[2] = 33
print("A: ", a)
print("B: ", b)

# Modifying B
# A:  [10, 55, 33, 40, 50]
# B:  [10, 55, 33, 40, 50]
