class Student:
    pass
# here we are making a class


harry = Student()
# we are making an object from student class
larry = Student()

harry.name = "Harry"
# we can make instance variable of an object like this
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["hindi", "physics"]
print(harry.name,harry.std)
print(harry.section, larry.subjects)
# if we will going to use 'larry.name' then it will through an error because we did not define the name for the larry
