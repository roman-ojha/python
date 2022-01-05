lis = ["john", "cena", "Randy", "orton", "sheamus", "khali", "jinder mahal"]

for item in lis:
    print(item, " and ", end="")

# we can do this mathod to join all the name
# but we have a seprate function join:

print("\n")
a = " and ".join(lis)
# this is the way to join

print(a, "other wwe superstars")
