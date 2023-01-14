# arr1=[1,2,3,4,5,6,7,8,9,10]

# print(arr1[0:3])
# arr1.append(4)
# print(arr1)
# print(arr1.count(2))
# arr1.reverse()
# print(arr1)

# tup1=(1,2,3,4,5,6,7,8,9,10)

# dict1={
#     "Name":"Roman",
#     "number":32,
#     "_id":43,
#     "Phone_Number":32,
#     "gender":"Male",
# }

# dict1[43]="num"
# del dict1[43]

# dict2=dict1
# del dict2["Name"]
# print(dict1) 
# print(dict2.get("number"))

# dict2.update({"Name":"Roman"})
# print(dict2.keys())
# print(dict2.items())
# print(dict2)


# set1={1,2,3,4,5,6}
# list1=[7,8,9,10,11]
# set_f_list=set(list1)
# print(set_f_list)

# set2=set()
# set2.add(5)
# set2.add(6)
# set2.remove(5)

# print(set2)

# x=int(input("Enter the value of x: "))
# y=int(input("Enter the value of y: "))

# if x>y:
#     print("X is greater then y")
# else:
#     print("Y is greater then X")


# list1=[1,2,3,4,5,6,7,8,9,10]

# if 11 in list1:
#     print("5 is in the list")
# else:
#     print("5 is not in the list")

# # print(list1)
# print(11 in list1)

# list = [3, 3, 2, 2, 39, 33, 35, 32]

# for key in list:
#     print(key,end=" ")



# dict1={
#     "Name":"Roman",
#     "number":32,
#     "_id":43,
#     "Phone_Number":32,
#     "gender":"Male",
# }

# for key,item in dict1.items():
#     print(key,item)

# i=0
# while(i<50):
#     print(i,end=" ")
#     i=i+1

# val=5

# def Operation(val1,val2,operator):
#     """This is the Docstrings"""
#     global val
#     val=43
#     if "+" in operator:
#         return val1+val2+val
#     elif "-" in operator:
#         return val1-val2
#     elif "*" in operator:
#         return val1*val2
#     elif "/" in operator:
#         return val1/val2
#     else:
#         print("Invalid operator")
#         return 0



# try:
#     print(43+43)
# except Exception as e:
#     print(e)
# print(Operation(5,6,"+"))
# print(val)
# print(Operation.__doc__)


# def factorial(num):
#     """This is the functin for the factorial"""
#     if num==1 or num==0:
#         return 1
#     else:
#         return num*factorial(num-1)

# print(factorial.__doc__)
# print(factorial(5))

# def sum(x,y):
#     return x+y

# res=lambda x,y:x+y

# print(res(1,2))

# list1=[1,2,3,4,5,6,7,8,9,10]


# print(res)

# def fun1(a1):
#     return a1[0]

# a1 = [[1, 40], [8, 6], [5, 23]]

# a1.sort(key=fun1)
# print(a1)

# import random

# print(random.random()*100)

# name="Roman"
# id=43

# print(f"my name is {name} and id is {id}")

# def sum(default_val,*args):
#     sum=default_val
#     for val in args:
#         sum=sum+val
#     return sum

# def printDect(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)

# dict1={
#     "name":"Roman",
#     "number":34
# }

# print(sum(1,2,3,4,5,6,7,8,9,10))

# printDect(**dict1)



# print("hello")

# if __name__=="__main__":
#     print("world")

# def func1(func2):
#     print("Before function 2")
#     func2()
#     print("After function 2")

# @func1
# def func2():
#     print("hello")



# if __name__=="__main__":
#     class Employee:
#         var1=32
#         def __init__(self,a,b,c):
#             self.a=a
#             self.b=b
#             self.c=c
#         def sum(self):
#             return self.a+self.b
#         def function1(a,b):
#             return a+b
        

#     obj1=Employee(13,2,3)
#     # obj1.name="Roman"
#     # obj1.id=43
#     # Employee.var1=43
#     # print(obj1.var1)
#     # print(Employee.var1)
#     # print(obj1.__dict__)
#     # print(Employee.__dict__)
#     res= obj1.sum()
#     print(res)

    

# class Complex:
#     def __init__(self,a=None,b=None):
#         self.a=a
#         self.b=b
    
#     def calculation(self,c1,c2):
#         self.a=c1.a+c2.a
#         self.b=c1.b+c2.b
    
#     def printdata(self):
#         print(f"A: {self.a}\nB: {self.b}")

# c1=Complex(1,2)
# c2=Complex(3,4)
# c3=Complex()
# c3.calculation(c1,c2)
# c3.printdata()

# class Complex:
#     a=10

#     @classmethod
#     def setdata(cls,value):
#         cls.a=value

#     @staticmethod
#     def count(cls):
#         return cls.a

# c1=Complex()
# c2=Complex()
# c1.setdata(5)

# print(c1.count(Complex))

class Student:
    def __init__(self,name,roll_No,class1):
        self.name=name
        self.roll_No=roll_No
        self.class1=class1
    def info(self):
        print(f"Student Detail:\nName: {self.name}\nRoll No.: {self.roll_No}\nClass:{self.class1}")


class Player(Student):
    def __init__(self,name,roll_No,class1,jersey_No):
        super().__init__(name,roll_No,class1)
        self.jersey_No=jersey_No

    def info(self):
        super().info()
        print(f"Jerser Number: {self.jersey_No}")

ply=Player("Roman",25,14,7)
ply.info()