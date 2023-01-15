import tut_46_If__name__equals_to_equals_to__main__useage_and_necessity
print(tut_46_If__name__equals_to_equals_to__main__useage_and_necessity.add(5, 3))
# so by importing module all the content will also exicute at the same time of that imported module so if you use print function in the import  module then all the print function will also exicute in the programm so we will going to see the print function and the result of all exicution of the import  module when you run the program to stop that execution we have to put all main content of import module in the main section in import module file
# now after putthing those content that are not need to be execute in the programm in the main section after that this program will not execute those section


""" 
NOTE:
# in import module file__name__ will be __main__
# But in this file
# name will be tut_46_If__name__equals_to_equals_to__main__useage_and_necessity
    that is why we use condition if __name__ == "__main__": to say that if __name__ will be __main__ only after that  block content nedd to execute and we know that in this file __name__will not be :
        tut_46_If__name__equals_to_equals_to__main__useage_and_necessity
 """
