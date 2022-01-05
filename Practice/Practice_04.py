# list1=[1,2,3,4,5,6]
# list1.append(7)
# # print(list1)

# tuple1=(1,2,3,4,5,6)
# # print(tuple1[4])
# # print(tuple1)

# dictionary1={
#     "name":"Roman",
#     "id":23
# }

# for item in list1:
#     print(item,end=" ")

# for index,value in enumerate(list1):
#     print(index,value)

# for i in range(0,len(list1),2):
#     print(list1[i])

# for index,value in dictionary1.items():
#     print(index,value)

# set1={1,2,3,4,5,6,7,8,9}

# print(set1)

# def sum(a,b):
#     return a+b

# list2=[int,float,str,print,sum,[1,2,3,4,5,6,7,8,9],{"name":"Roman","id":12},43,43,65,"Roman","Ojha",54.7]
# # print(list2)

# print(list2[0])
# list2[3]("Hello")
# print(list2[4](1,2))
# for item in range(0,len(list2[5]),2):
#     print(item)


# name="Ojha"
# print(dictionary1.items())

# def function1(sum):
#     """This is the DocString"""
#     global name
#     name="Roman"
#     sum(f"Hello, My name is {name}")

# def sum():
#     return print

# try:
#     a=1+"b"
#     function1(sum()),
#     print("Trying")
# except Exception as e:
#     print("This is the error:",e)



# print(function1.__doc__)
# print(name)

# print("Roman".join("Ojha"))

# list1=[1,2,3,4,5,6,7,8,9]

# try:
#     a="Roman".join(list1),
#     print("Trying")
# except Exception as e:
#     print(e)
#     try:
#         print(a),
#         print("trying")
#     except Exception as e:
#         print(e)


# name=['Roman',"ojha"]

# print(" and ".join(name))

# def shout(text):
#     return text.upper()

# def whisper(text):
#     return text.lower()

# def greet(func):
#     greeting=func("""hello, EVERYONE""")
#     print(greeting)

# greet(shout)
# greet(whisper)

# def function1(func):
#     print(func())



# @function1
# def sum(a,*arg):
#     sum=a
#     for value in arg:
#         sum=sum+value
#     return sum

# operationSwitch={
#     ["add","a","b"]:sum(),
#     "sub":4,
# }

# operationSwitch.get("add")

# def function1(func):
#     print(func(printj))


# @function1
# def pf(print):
#     return print

# pf(print)


# def printFunction(func):
#     return print(func(1,2))


# @printFunction
# def sum(a,b):
#     return a+b

# sum(1,2)


# from _typeshed import Self


# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def displayData(self,name,id):
#         print("Name:",name,"\nID:",id)


# employee1=Employee("Roman",12)
# # employee1.displayData()

# # @smart_change 

# def smartChange(func):
#     def innerFunc(name,id):
#         name,id=id,name
#         return func(name,id)
#     return innerFunc

# employee1.displayData=smartChange(employee1.displayData)

# employee1.displayData("Roman",12)
    
# class Complex:
#     a=5
#     b=6
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     @classmethod
#     def setData(cls,a,b):
#         cls.a=a
#         cls.b=b

#     # def displayData(self):
#     #     @classmethod
#     #     def innerDisplay(cls,self):
#     #         return print(cls.a+self.a)
#     #     return innerDisplay
#     def displayData(self):
#         print(Complex.a+self.a,Complex.b+self.b)



# complex1=Complex(1,2)
# complex1.displayData()
# complex1.name="roman"
# complex1.id=12
# print(complex1.name,complex1.id)
# Complex.a=10
# print(Complex.a)


class Number:
    b=6
    
    def __init__(self,a=None):
        self.a=a

    def displayNumber(self):
        print(self.a,self.b)

number1=Number(5)
number1.displayNumber()
# print(Number.b)