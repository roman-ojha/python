f1 = open("Python/Code_With_Harry_Tutorial/Files/tut_26.txt")

try:
    f = open("random_file_name.txt")
except EOFError as e:
    # EOFError is one type of error
    # end of file error
    print(e)
except IOError as e:
    # IOError is also one type of an error
    print(e)
else:
    # here else will run if except will not run and if except will run then else will not run
    print("this will run only if except will not running")

finally:
    # here finally will definetly run
    print("The will run anyway")
    # f.close()
    f1.close()
    # so here we close the file in finnally because if file will open in try block then file willclose
