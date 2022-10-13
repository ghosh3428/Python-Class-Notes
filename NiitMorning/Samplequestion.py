#generate a series between 0 to n
#                for i in range(0, n+1 ,1)
#find the sum of even numbers
#find the sum of odd numbers


n = int(input("Enter the end value : "))

sumE = 0
sumO = 0

# for range operator
# default start value is 0
# default step value is 1
#for i in range(0, n+1 ,1)

for i in range( n+1 ):
    print(i , end="   ")
    if i%2 == 0 :
        sumE = sumE + i
    else :
        sumO = sumO + i

print()
print("Sum of Even Numbers is :" , sumE)
print("Sum of Odd Numbers is  :" , sumO)

