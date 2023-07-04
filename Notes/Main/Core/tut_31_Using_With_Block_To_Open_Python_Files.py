with open("Python/Code_With_Harry_Tutorial/Files/tut_31.txt") as f:
    # this is also the way to open the file in this situation we don't have to close the file , with block will automatically handle it
    a = f.readline()
    print(a)


f = open("Python/Code_With_Harry_Tutorial/Files/tut_31.txt", "rt")
print(f.read())
# in here we can again read the file because with block had already close that file inside the block and when you are outside the block then you can access the file agian and in here we have to close the file because we are outside the with block
f.close()
