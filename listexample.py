# create a list
# 1) list()
# 2) []

mylist = list()

mylist2 = []

print(mylist)
print("---------------------------------------------")

# add data to a list
# 1) append(data) -> add a single data at the end of the list
# 2) extend(multiple data)) -> adds multiple data at the end of the list
# 3) insert(index , data) -> adds data at the specified index

#Append

mylist.append("Niit")
mylist.append("Kolkata")
mylist.append("West Bengal")

print(mylist)
print("---------------------------------------------")


#Extend

mylist.extend([45,78,90,True,"Jadavpur"])

print(mylist)
print("---------------------------------------------")

#insert(index , data)
#adding a single data
mylist.insert(1 , 700032)

print(mylist)
print("---------------------------------------------")


# Remove(data) -> removes the specified data

mylist.remove("Jadavpur")

print(mylist)
print("---------------------------------------------")

# del[index] -> removes a single data at the specified index

del mylist[0]

print(mylist)
print("---------------------------------------------")

# del[start : end :step] -> removes multiple data 

del mylist[3:6:1]

print(mylist)
print("---------------------------------------------")


# pop(index) -> removes and return the data the specied index 

data = mylist.pop(1)
print(data)
print(mylist)
print("---------------------------------------------")

# clear() -> removes all the data

mylist.clear()

print(mylist)
print("---------------------------------------------")


