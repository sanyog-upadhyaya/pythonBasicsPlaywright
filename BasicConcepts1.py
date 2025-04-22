from traceback import print_tb

print('Hello')

# comments
# variable

a =3;
print(a);

# multiple variable declaration in single line
b,c,d = 5,4,3;
print(b,c,d);

# print("value is"+b)  this will throw error
# we use format method to concatenate two diff data types for same data type + will work for
# concatenation

print("{}{}".format("value is ", b))

# to know what type of data type is assigned to variable by python we use type method

print(type(b))

#data types in python numeric, list, string, complex, tuple, dictionary

# list

values = [1, 2, "name", 4, 5]
# list is a data type that allows multiple values and can be diff data types
print(values[0])
print(values[-1]) # it will print the last value of the list (-1)
print(values[1:3])

values.insert(3, 'sanyog') # insertion to list
print(values)

values.append("Upadhyaya") # append at the last value of list
values[2] = "My Name is" # updation
del values[0]  # deletion

print(values)

# tuple

# list and tuple are almost same except tuple data type is immutable but
# list data type is mutable i.e when we can declare tuple, we can update the tuble
# we cant modify but in list we can and declare tuple is () and list is []

val = (1,3,"name",4)

# print(val.append("san")) this will throw error

# Dictionary

# is an unordered sequence of data of key-value pair form, it is similar to hashtable
# It is written in curly braces in key-vale form, it is useful to retrieve data in an
# optimized way among a large amount of data

dic = {"a":2, "name":"sanyog", 2:"Uapdhyaya"}
print(dic)
print(dic["a"])
print(dic[2])