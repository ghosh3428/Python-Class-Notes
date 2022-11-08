#accept 10 numbers and place even on the right
#and odd on the left

mylist = list()

for i in range(10):
    print("Enter data at position/index",i)
    mylist.append(int(input()))
print(mylist)

for i in range(10):
    if(mylist[i]%2 == 0):
        for j in range(i+1,10):
            if(mylist[j]%2 == 1):
                for k in range(j , i,-1):
                    temp = mylist[k]
                    mylist[k] = mylist[k-1]
                    mylist[k-1] = temp
                break
print(mylist)              
        

        
    
