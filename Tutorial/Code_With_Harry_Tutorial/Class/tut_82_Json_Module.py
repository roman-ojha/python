
import json
# the full form of the json is java script object notation
# in json you have to use double cotes""  and json doesnot have a comments

data = '{"var1":"harry", "var2":56}'
# this is one kind of the data json have
print(data)

parsed = json.loads(data)
# json.loads will load thedata
print(parsed)
# we are making the data into jason
# we can say that "we make the jason parsed"
print(type(parsed))
# parsed is a dictionary

# your task
# Task 1 - json.load?
# you have to inquiarry your self


data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    # here this is the tuple which javascript will not understand
    "isbad": False
    # and here we use "False" but in java script we din't have "F" incapital so this will throw an error

}

jscomp = json.dumps(data2)
# to make the javascript compatible we use dumps function
# now this become the json object
print(jscomp)

# your task:
# Task 2 = what is sort_keys parameter in dumps
