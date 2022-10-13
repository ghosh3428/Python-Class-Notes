set1={"Lion","python",456,85.76}
print (set1)

print("------------------------------------")

#4. Write a Python program to remove item(s) from a given set.

set1.remove(456)
print(set1)

print("------------------------------------")

#6. Write a Python program to create an intersection of sets.
set2={124,267,321,582,691,759,159,482}
set3={123,267,320,582,690,759,150,482}
set4=set2.intersection(set3)
print (set4)

print("........................................")
set4=set2.union(set3)
print(set4)
      
