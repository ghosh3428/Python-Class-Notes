num1 = int(input("Enter a number : \n"))
num2 = int(input("Enter a number : \n"))
num3 = int(input("Enter a number : \n"))

#nested if
#outer if
if num1>num2:
    #inner if
    if num1>num3 :
        print(num1 , "is greater")
    else :
        print(num3 , "is greater")
elif num2>num3:
    print(num2 , "is greater")
else:
    print(num3 , "is greater")
