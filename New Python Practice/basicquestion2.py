#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
num1=17
num2=int(input("Enter a number 2 :"))

difference=num2-num1
if num2>num1:
    print(difference*2)
else:
    print(abs(difference))
