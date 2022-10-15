#Write a Python program to test whether a number is within 100 of 1000 or 2000

num1=int(input("enter a number :"))
if 900<=num1<=1100:
    print(" Number is within 100 of 1000")
elif 1900<=num1<=2100:
    print(" Number is within 100 of 2000")
else:
    print("Number is not within 100 of 1000 or 2000")
    
