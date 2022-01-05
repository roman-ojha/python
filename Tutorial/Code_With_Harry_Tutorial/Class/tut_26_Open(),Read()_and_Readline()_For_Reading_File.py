"""  open function """
# f = open("Python/Code_With_Harry_Tutorial/Files/tut_26.txt", "r") #-> this is the default mode so nothing will change
# f = open("Python/Code_With_Harry_Tutorial/Files/tut_26.txt", "rt") # -> this is also the default mode
f = open("Python/Code_With_Harry_Tutorial/Files/tut_26.txt", "rb")
# rb mode will read the file in binary form
# here f is a file pointer
""" read function """
# content = f.read()
# print(content)

# content = f.read(3)
# print(content)
# read(3) will going to read the three character

# content = f.read(3)
# print(content)
# now  this will read another three character

# content = f.read(34455)
# print("1", content)
# content = f.read(34455)
# print("2", content)
# here because of not having that much charecter another read function will not apply


""" For itrating line by line """
# for line in f: # if we want to print line by line then we have to itrate f not content, content will itrate character by character
#     print(line, end="")
# print(content)

"""  readline function """
# print(f.readline())
# this will going to read first line of the file

# print(f.readline())
# now this will going to print the  second line of the file

""" readlines function """
print(f.readlines())
# this will going to print the list of the line contain  in  the file

""" close function """
f.close()
# we have to close if we oppned that file
