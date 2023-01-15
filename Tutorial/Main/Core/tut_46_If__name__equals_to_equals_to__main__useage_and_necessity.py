def printhar(String):
    return f"this is the string {String}"


def add(num1, num2):
    return num1+num2+5


print("and the name is:", __name__)
# in here __name__ will be __main__
# But in the imported file
# name will be tut_46_If__name__equals_to_equals_to__main__useage_and_necessity
if __name__ == "__main__":
    print(printhar("Roman"))
    o = add(4, 6)
    print(o)
