""" 
What Is Polymorphism?
In basic English language, Polymorphism means to exist in different states. The same object or thing changing its state from one form to another is known as polymorphic. A same function or method, being used differently in different scenarios can perfectly describe polymorphism. It occurs mostly with base and derived class.  

Understanding Polymorphism in Python
The concept of polymorphism has very strong ties with method overriding concept that we will learn in the next Tutorial i.e tutorial#65 of this course along with super() function. In Python, it is mostly related to objects or the values of variables that are assigned in different classes. For example, if a method in the child class that has the same name as the methods in the parent class and also they take the same number of variables as parameters, then the child class will inherit the methods from the parent class and will override the method too. Meaning that the compiler will execute the method in the child because it will be the first place it looks while searching for the method when called. By overriding a method, we can also add some more functionalities in it, so in a way modifying the method in the child class but letting it remain the same in the parent class.
 """
"""

For example:
len("Python") # returns 6 as result
len([1,2,3,4,5,6,7,8,9]) # returns 9 as result

 """

print(5+6)
# here the value will be 11
print("5" + "6")
# her the value will be 56
# but we did the same thing , we add 5+6 then why result is different , so this is called as Polymorphism in which we get the different result by doing the same thing , here it change of form because in first we add integer and in second we add string that's why it change the form of performing thing


# Abstraction
# Encapsulation
# Inheritance
# Polymorphism
