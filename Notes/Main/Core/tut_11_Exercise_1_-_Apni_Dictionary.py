""" 
create a dictionary and take input from the user and return the meaning of the woed from the dictonary
 """
print("Dictionary:")
d1 = {
    "roman": "Roman numerals are defined as combinations of the letters I, V, X, L, C, D and M which are used in various orders to stand for a specific number",
    "process": "a series of actions or steps taken in order to achieve a particular end.",
    "history": "the whole series of past events connected with a particular person or thing.",
    "keyboard": "a panel of keys that operate a computer or typewriter.",
}
print("Enter the word to find the meaning of that word")
inp = input()

print(d1[inp])
