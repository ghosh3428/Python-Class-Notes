#8Write a Python program to create set difference.
set1={"cat","dog","cow",204,347,574}
set2={"cat","tiger","cow",204,312,572}
set3=set1.difference(set2)
print(set3)
print("............................................")
#10. Write a Python program to check if a set is a subset of another set.
set4={1,2,3,4,5,6,7,8,9,10}
set5={3,4,5,6,7}
if set5.issubset(set4):
   print("True")
else :
   print("False")
print("-------------------------------------------------------------")
#11. Write a Python program to create a shallow copy of sets.

print("--------------------------------------------------------------")

#12. Write a Python program to remove all elements from a given set.

set4.clear()
print(set4)

print("------------------------------------------------------------")

#Write a Python program to find maximum and the minimum value in a set.

t=max(set5)
print(t)
t1=min(set5)
print(t1)

print("--------------------------------------------------------------")

#Write a Python program to find the length of a set.

s = len( set1 )
print(s)

print("----------------------------------------------------------------")

#Write a Python program to check if a given value is present in a set or not.
if 5 in set5:
    print("Data Found")
else:
    print("Data Not found")






