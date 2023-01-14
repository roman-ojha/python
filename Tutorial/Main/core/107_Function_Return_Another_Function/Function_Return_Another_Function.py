# Function return another function


# =====
def desc():
    def show():
        print("Show function")

    print("Desc function")
    return show


show = desc()
show()


# =====
def desc(show):
    print("Desc function")
    return show


def show():
    print("Show function")


show = desc(show=show)
show()
