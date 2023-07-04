# First Create empty list
a = []

# Then ask user for it's size and parsing into int and storing into n
n = int(input("Enter size of List: "))

for i in range(n):
    # Input element one by one
    a.append(int(input("Enter Element: ")))


# Print list
print("List: ")
for element in a:
    print(element)
