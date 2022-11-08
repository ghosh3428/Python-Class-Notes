marksheet = list()

for i in range(2):
    print("Enter details of Student" , (i+1))
    student = list()

    print("Enter student Name : ")
    student.append(input())

    print("Enter Roll Number : ")
    student.append(input())

    print("Enter Maths Marks : ")
    student.append(int(input()))
    print("Enter English Marks : ")
    student.append(int(input()))
    print("Enter Physics Marks : ")
    student.append(int(input()))
    print("Enter Chemistry Marks : ")
    student.append(int(input()))
    print("Enter Biology Marks : ")
    student.append(int(input()))

    student.append(sum(student[2:7]))

    student.append(round(student[7] / 5 , 2))

    marksheet.append(student)

for student in marksheet:
    print("-----------------MARKSHEET--------------")
    print("Student Name    :" ,student[0])
    print("Roll Number     :" ,student[1])
    print("Maths Marks     :" ,student[2])
    print("English Marks   :" ,student[3])
    print("Physics Marks   :" ,student[4])
    print("Chemistry Marks :" ,student[5])
    print("Biology Marks   :" ,student[6])
    print("Total Marks     :" ,student[7])
    print("Percentage      :" ,student[8])
    print("----------------------------------------")


