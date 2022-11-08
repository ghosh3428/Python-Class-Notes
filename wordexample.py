word = list()
print("Enter 5 Words :")
for i in range(5):
    word.append(input())

vowelcount = list()
for data in word:
    data = data.upper()
    count = 0
    for i in data:
        if i in "AEIOU":
            count = count + 1
    vowelcount.append((data,count))

print(vowelcount)

