
import pickle
# pickling means presevation
# here pickle means preserved and store

# ******************* Pickling a python object *******************

# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# we are trying to pack this data in to pkl file to preserve and use in future

# file = "mycar.pkl"
# we can make the file like this

# fileobj = open(file, 'wb')
# we open that file , and we have to open the file in binary mode

# pickle.dump(cars, fileobj)
# this will dump the data in the file
# note: this will note take a file but it will take a file object

# fileobj.close()

# now we can read the pkl file like this
file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))

# learn yourself
# pickle.loads() = ?
# pickle.load() = ?
