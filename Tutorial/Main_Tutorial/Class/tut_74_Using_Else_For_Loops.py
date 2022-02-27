khana = ["roti", "sabzi", "chawal"]

# there is the two way to end for loops
# -> one is when itration will in like in list when list item will end then for loop will ends
# -> another way is to break for loop by giving some conditions
# so in else for loop ,it will go to else when for loop is ends normally after itration

for item in khana:
    print(item)

else:
    print("This for loops ends properly")
    # here else part will apply when for loops will end normaly

for item in khana:
    print(item)
    break

else:
    print("This for loops ends properly")
    # here else part will not apply because we use break statement so for loops don't ends normaly


# we can use else for loops like this

for item in khana:
    if item == "chawal":
        break
    print(item)
else:
    print("your item was not found")
