mylist=[1,"a",2,"b",3,"c",4,"d"]

mylist2 = mylist.copy()

mylist[1] = "Niit"

mylist[3:4:1] = ["Kolkata" , "West" , "Bengal"]

print(mylist)
print(mylist[5])
print(mylist[0:7:2])

print(mylist[1:8:2])
print(mylist[-1])
print(mylist[-2])
print(mylist[::-1])

print(mylist.index("West"))

num = [*range(1,11,1)]
print(num)


num =[1,3,2,5,7,34,89,23,12,90]
num.sort(reverse=True)
print(num)







