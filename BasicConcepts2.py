# if else loop
# : is used for start of the condition and indentation should be correct
name = "Sanyog"

if name == "Sanyog":
    print("name is Sanyog")
else:
    print("name is not Sanyog")

print("COMMON")

# add value in dictionary

dict ={}

dict["name"]="sanyog"
dict["lastname"]="Upadhyaya"

print(dict)
print(dict["lastname"])

# for loop

obj = [1,9,3]
for i in obj:
    print(i)
    print(i*3)

summation =0
for j in range(1,5): #range(i,j) -> i to j-1 but by default j++
    summation += j
    print(j)
print(summation)


for j in range(1,5,2): # here 1 is start, 5 is j-1 that end index 4 and 2 is j+2
    print("{}{}{}".format("number is ", j, "Iterated interval 2" ))

# loops