#Write a C program to input electricity unit charges and
#calculate total electricity bill according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill


unit = int(input("Enter the amount of unit consumed :"))

if unit <= 50:
    charge = unit*0.5
elif unit<=150:
    charge = 50*0.5 + (unit-50)*0.75
elif unit <=250:
    charge = 50*0.5 + 100*0.75 + (unit-150)*1.2
else:
    charge = 50*0.5 + 100*0.75 + 100*1.2 + (unit-250)*1.5


charge = charge + charge*20/100

print("Final Bill : Rs" , charge)

