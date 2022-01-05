f = open("Python/Code_With_Harry_Tutorial/Files/tut_30.txt")
# open function will open the file until program ends so we can find the realtime update of that file
print(f.tell())
# this will going to tell that where the file pointer is  right now according to the character count
print(f.readline())
print(f.tell())
f.seek(0)
# seek function will reset the file pointer and put at that position where we want to get the content
print(f.tell())
# now  again  tell function will return 0 because we are now at  the first character
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(58)
# here now file pointer come at the character 58
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())

f.close()
