#Accept radius and find the area and perimeter of a circle

#input
pi = 3.14

print("Enter radius of the circle :")
r = int(input())


#process
area = round(pi *(r**2) , 2)
perimeter = round(2*pi*r , 2)


#output
print("Area of the circle is        :",area)
print("Perimeter of the circle is :" , perimeter)
