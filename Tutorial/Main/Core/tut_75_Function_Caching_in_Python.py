import time
from functools import lru_cache
# here lru_cache is a deocrator


def some_work(n):
    # some task take n second
    time.sleep(n)
    return n


if __name__ == "__main__":
    print("Now running some work")
    some_work(3)
    # here this will take 3 second to complete the task if this function need to be call a lot in the programm then it will take a lot of time to complete the program so we use a function caching we store the return value or some data in cach and use it when i need
    print("done")
    print("calling again")
    some_work(3)
    print("called again")
    # we can do by function caching:


@lru_cache(maxsize=3)  # -> maxsize means how many value do you want to cach
def some_work1(n):
    # some task take n second
    time.sleep(n)
    return n


if __name__ == "__main__":
    print("Now running some work1")
    some_work1(3)
    # here it will take 3 second to complete but after that it will cach and store that data so it will complete imidiatlly
    print("done")
    print("calling again")
    some_work1(3)
    some_work1(1)
    some_work1(2)
    some_work1(4)
    # now we have alrady say that maxsize will be 3 so here we run four function and value is different 3->1->2->4-> so here only three value is in cach 1,2,4 so if we call some_work1(3) again then it will take 3 second again because 3 is not save in cach
    print("called again")
    # we can do by function caching:
    some_work1(3)
