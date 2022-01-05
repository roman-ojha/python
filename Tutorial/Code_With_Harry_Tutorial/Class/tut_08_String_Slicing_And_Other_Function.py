mystr = "harry is a good boy"
print(mystr)
# in python index will start from 0
print(mystr[4])  # this will going to print the charecter at index [4]
# -> string slicing
print(mystr[0:4])
# here 4 will exclude of you want to print charecter form o-4 then you have to do this
print(mystr[0:5])
print(len(mystr))
# this will going to get the length of the string if the string len is 19 then string start form 0-18
print(mystr[0:100])
# we can do this if we dont have 100 index string also
print(mystr[0:5:2])
# after including 2 now it will print form 0 to 4 but escaping 1 ,1 charecter from that string
print(mystr[0:])
# this will going to print all of your charecter
print(mystr[:5])
# if we dont put a index number at the first then it will automatically put 0 at the first
print(mystr[:])
# this will also going to print the hole string
print(mystr[::])
# this will put 1 for the escaping charecter so, by doing this this will going to print the whole string //print(mystr[::1])
print(mystr[::6544])
print(mystr[-4])
# this will count from the end
print(mystr[-4:-1])
print(mystr[15:18])  # are same for this string
# -1 will start from end of the string
print(mystr[::-1])
# here by using - this will going to inverse the string
print(mystr[::-2])
# this will going to inverse the string and escaping 1 ,1 charecter

""" Other function """
print(mystr.isalnum())
# there is another datatype in python that is bollean
# in this setuation this will return false because we have space include in string
# if string doesnot include space then it will going to return true
print(mystr.isalpha())
# this will check alpha numeric and in this case it will be false because there is space in string
print(mystr.endswith("boy"))
# this will return true because string is ends with boy
print(mystr.count("b"))
# this will going to count the charecter b in the string
print(mystr.capitalize())
# this will going to capital to first letter in the string
print(mystr.find("is"))
# this will going to find the "is" string in the given string and return the index value
print(mystr.lower())
# this will going to convert string in lower case
print(mystr.upper())
# this will going to convert string in upper case
print(mystr.replace("is", "are"))
