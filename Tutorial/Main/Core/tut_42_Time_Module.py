import time

""" To get the time of exticution of program """

initial = time.time()
# here time() function will give no. of tik
# 1 tik == 1 second
print(initial)
k = 0
while (k < 1115000):
    print("", end="")
    k += 1
print("\nwhile loops run in: ", time.time()-initial, " Seconds")
# here we will going to get the time taken by while loops
initial2 = time.time()
for i in range(1115000):
    print("", end="")
print("\nFor loops run in: ", time.time()-initial2, " Seconds")
# here we will going to get the time taken by the for loops
# we can go to the internet and search for the time module and function of the time module

""" Real time function """

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
# this will give the local time and present time
# here time.time return tiks form older time and time.localtime() will conver it into local time if we want print the return value return by the time.localtime() then it will be a tuple that's why asctime will convert that localtime into presentable time
localtime1 = time.localtime(time.time())
print(localtime1)
# if we only print this then we will get tuple

""" sleep function """

print(initial)
k = 0
while (k < 2):
    print("", end="")
    time.sleep(2)
    # when time.sleep function will executed then the program will sleep or stop to porform for a 2 second
    k += 1
print("after while loops sleep")
initial2 = time.time()
for i in range(2):
    print("", end="")
    time.sleep(2)
print("after for loops sleep")
