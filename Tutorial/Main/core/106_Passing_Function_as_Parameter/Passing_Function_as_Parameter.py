# Pass function as parameter

def desc(show):
    show()
    print("Desc function")


def show():
    print("Show function")


desc(show=show)
