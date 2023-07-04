class Mobile:
    fp = "Yes"  # Class variable

    # Accessing class variable inside the class using '@classmethod'
    @classmethod
    def is_fp(cls):  # Class method
        # Here we will get 'cls' rather then the object instance
        print(cls.fp)


realMe = Mobile()

# Calling class method
Mobile.is_fp()
# Yes

# Accessing Class variable Outside class
print(Mobile.fp)
# Yes


# Changing Class variable value
Mobile.fp = "No"
print(Mobile.fp)
# No

redMi = Mobile()
print(Mobile.fp)
# No
