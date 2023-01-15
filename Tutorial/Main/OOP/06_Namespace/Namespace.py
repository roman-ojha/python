class Mobile:
    fp = "Yes"  # Class Variable
    # Mapping 'fp' to "Yes" it is an class namespace

    @classmethod  # Class Method
    def is_fp(cls):
        print("Finger Print: ", cls.fp)  # Accessing Class Variable


# Mapping object to 'fp' is an instance namespace
realMe = Mobile()
readMi = Mobile()
honor = Mobile()

print("Class Fp: ", Mobile.fp)
# Class Fp:  Yes
print("RealMe: ", realMe.fp)
# RealMe:  Yes
print("ReadMi: ", readMi.fp)
# ReadMi:  Yes
print("Honor: ", honor.fp)
# Honor:  Yes

# Modifying using class:
Mobile.fp = 'No'
print("Class Fp: ", Mobile.fp)
# Class Fp:  No
print("RealMe: ", realMe.fp)
# RealMe:  No
print("ReadMi: ", readMi.fp)
# ReadMi:  No
print("Honor: ", honor.fp)
# Honor:  No


# Modifying using instance object
readMi.fp = 'Not working'
print("Class Fp: ", Mobile.fp)
# Class Fp:  No
print("RealMe: ", realMe.fp)
# RealMe:  No
print("ReadMi: ", readMi.fp)
# ReadMi:  Not Working
print("Honor: ", honor.fp)
# Honor:  No
