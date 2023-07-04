# copy(): =====
a = [10, 20, 30, 40, 50]

# Copying 'a' list into 'b'
b = a.copy()
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
# B:  [10, 20, 30, 40, 50]

print("Modifying B")
b[2] = 33
print("A: ", a)
print("B: ", b)
# Modifying B
# A:  [10, 55, 30, 40, 50]
# B:  [10, 20, 33, 40, 50]

# clone: =====
a = [10, 20, 30, 40, 50]

# Cloning 'a' list into 'b'

b = a[:]
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
# B:  [10, 20, 30, 40, 50]

print("Modifying B")
b[2] = 33
print("A: ", a)
print("B: ", b)
# Modifying B
# A:  [10, 55, 30, 40, 50]
# B:  [10, 20, 33, 40, 50]
