#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))

sum=num1+num2+num3

if num1==num2==num3:
    print(sum*3)
else:
    print(sum)

print("________________________________________________")



    
