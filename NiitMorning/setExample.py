mytupple1= ("Ajay" , "Vijay" , "Kapil" , 123 , 34.56 , True,"Ajay" , 123)
print(mytupple1)

#Add a data
# Tupple -> +
mytupple1 = mytupple1 + ("Kolkata" ,)
print("-------------------------------------------")

myset1= {"Ajay" , "Vijay" , "Kapil" , 123 , 34.56 , True,"Ajay" , 123}
print(myset1)

print("---------------------------------------------------")

#Set -> add(data)
myset1.add("Kolkata")
print(myset1)


print("-------------------------------------------------------")

set1 ={1,2,3,4,5,6,7,8,9,10}
set2 = {1,3,5,7,9,11,13,15,17,19}

print("set1 :" , set1)
print("-------------------------------------------------------")
print("set2 :" , set2)
print("-------------------------------------------------------")
#Union
# | - > union operator
# union() -> returns a new set

print("Union Operator :" , set1 | set2)
set3 = set1.union(set2)
print("Union Function :" , set3)

print("-------------------------------------------------------")

#Intersect
# & -> intersect operator
# intersection() function -> returns a new set
print("Intersect Operator :" , set1 & set2)
set3 = set1.intersection(set2)
print("Intersect Function :" , set3)


print("-------------------------------------------------------")

#minus
# - -> minus operator
# difference() function -> returns a new set

print("set1 - set2 :" , set1 - set2)
set3 = set1.difference(set2)
print("set1.difference(set2) :" , set3)

print("-------------------------------------------------------")

#except
# ^ ->except operator

print("set1 ^ set2 :" , set1 ^ set2)

print("-------------------------------------------------------")
#difference_update() -> update the first set
set1.difference_update(set2)

print("Set1 :" , set1)
print("-------------------------------------------------------")

#Delete
#clear() -> removes all data
#pop() -> removes the data at the first position
#discard(data) -> removes the specified data
#remove(data) -> removes the specified data

set2.pop()
print("set2(pop) :" , set2)
print("-------------------------------------------------------")

set2.discard(11)
print("set2(discard - 11) :" , set2)
print("-------------------------------------------------------")

set2.remove(9)
print("set2(remove -9) :" , set2)
print("-------------------------------------------------------")

set2.clear()
print("set2(clear) :" , set2)



