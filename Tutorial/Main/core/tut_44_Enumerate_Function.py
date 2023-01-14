li = ["Bhindi", "Aloo", "Chopsticks", "chowmein"]

i = 1
for item in li:
    if i % 2 is not 0:
        print(f"Jarvis please buy {item}")
    i += 1

# This is the normal function to itrate item form the data
""" by Enumerate function """

for index, item in enumerate(li):
    # by using enumerate we are not using 'i' variable becasue now we can use 'index'
    if index % 2 == 0:
        print(f"Jarvis Please buy {item}")

# index will itrate index of the list and the item will itrate item
