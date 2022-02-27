
import os
# here also os means operating system
# in os module we can do , if we want to rename the file,if we want to look to the file that what what filex that file have,and if we want to open the folder and if we want to rename the file

# print(dir(os))
# this will show you that what method and attribute that you have in os module

# print(os.getcwd())
# this will show you , what is your current working directory

# os.chdir("C://")
# like this we can change the current working directory
# but we have the current working file in the same place where you have erlyer but now this program will consider c:// as a directory

# print(os.getcwd())
# here you can see the change

# f = open("harry.txt")
# if you are trying to open the file from the this direntory then it will thorw an error

# print(os.listdir("C://"))
# this will give all the file and the folder of the current working directory
# this will return list

# os.mkdir("this")
# we can make the folder in the current working directory

# os.makedirs("This/that")
# we can make multiple folder inside to inside by this

# os.rename("harry.txt", "codewithharry.txt")
# if we want to rename the file and the folder

# print(os.environ.get('Path'))
# you can read environment variable then you can do like this

# print(os.path.join("C:/", "/harry.txt"))
# this will join the path in optimal way that we dont have to worry about slash"/""

# print(os.path.exists("C://Program Files2"))
# this will show you that , do this kind of path is exis or not
# and this will return boolean


# print(os.path.isfile("C://Program Files"))
# this will show you that , is the path is a file or not
# it will also return boolean
