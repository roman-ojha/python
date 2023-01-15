""" Write mode """
# f = open("Python/Code_With_Harry_Tutorial/Files/tut_28.txt", "w")

# in here w mode is the write mode which will help to write the content in the file if that file has alrady created but if the file is not created then w mode will make the new file in that path and write the context that user give
# and this mode will remove the older content from the file  and add new one

# f.write("Harry bhai bahut achhe hain")

""" Append mode """
# f = open("Python/Code_With_Harry_Tutorial/Files/tut_28.txt", "a")
#  append mode will not remove the older file and append the new content at the end of the older content

# f.write("Harry bhai bahut achhe hain\n")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# this will print the number of character that are write in the file

""" Read and Write mode  """
f = open("Python/Code_With_Harry_Tutorial/Files/tut_28.txt", "r+")
# r+ is the mode where you can read the content and write the content
print(f.read())
# this will going to read the file
print(f.write("Thank you\n"))
# this will going write the contect in the file and not delete the older content we are reading the file at  the begining so we cant read the write file when first run


f.close()
