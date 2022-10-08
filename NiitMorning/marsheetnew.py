#input part
name = input("Enter Student Name : ")
roll_number = int(input("Enter Roll Number : "))
my_class = int(input("Enter Class : "))
section = input("Enter Section : ")
eng = int(input("Enter English Marks : "))
maths = int(input("Enter Maths Marks : "))
sci = int(input("Enter Science Marks : "))
comp = int(input("Enter Computer Marks : "))
hindi = int(input("Enter Hindi Marks : "))


#process Part
total = eng + maths + sci + comp + hindi
average = total/5

if average >= 90:
    grade = 'A+'
elif average >=80:
    grade ='A'
elif average >=70:
    grade ='B'
elif average >=60:
    grade ='C'
elif average >=50:
    grade ='D'
elif average >=40:
    grade ='E'
else:
    grade ="Fail"


print("--------------------MARKSHEET------------------")
print("Student Name    :" , name)
print("Roll Number       :" , roll_number)
print("Class                 :" , my_class)
print("Section              :" , section)
print("Maths Marks       :" , maths)
print("Science Marks    :" , sci)
print("Computer Marks :" , comp)
print("Hindi Marks        :" , hindi)
print("English Marks     :" , eng)
print("Total Marks        :" , total)
print("Percentage         :" , average)
print("Grade                :" , grade)
print("----------------------------------------------------")
