
def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)
        # here we are saying that we are using searcher as a coroutines and the thing that send to the searcher that value will come to an yield
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")


search = searcher()
# because searcher is not a function we make an search as a instance of the searcher
print("search started")
next(search)
# in this method search will start
print("Next method run")
search.send("harry")
# here it will take 4 second to search the "harry" text in the book and after the so the result does it have or not

# input("press any key")
# search.send("harry and")
# now in here it will not search that whole text because it had alrady completed to read and now it will imedetily search and show an result
# after one search only while loops is working

# input("press any key")
# search.send("thi si")
# this will also search instantlly

# input("press any key")
# search.send("joker")
# same.....

# input("press any key")
# search.send("like this video")
# same......

search.close()
# you can closs search like this

# search.send("harry")
# because we close coroutines it will through an error
