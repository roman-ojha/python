# Nested function

def disc():
    def show():
        def hello():
            print("Hello function")
        print("Show function")
        hello()
    print("Disc Function")
    show()


disc()


def disc():
    def show():
        def hello():
            return "Hello function"
        return hello() + " Show function"
    return show() + " Disc Function"


print(disc())
