a = [1, "Roman", 400.21, -30]

# for <single_elm_iterator_value> in <from_list>
for element in a:
    print(element)

# Using index number:
# length of the list
n = len(a)
for i in range(n):
    print("index: ", i, " element: ", a[i])
