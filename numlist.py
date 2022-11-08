num = list()
print("Enter 5 numbers :")
for i in range(5):
    num.append(int(input()))

for data in num:
    if data%2 == 0:
        for i in range(1,data,2):
            print(i , end="\t")
    else:
        for i in range(2,data,2):
            print(i , end="\t")
    print()

