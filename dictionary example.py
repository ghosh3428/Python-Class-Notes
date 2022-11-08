marksheet = dict()

marksheet["Name"] = "Rohan Mishra"
marksheet["Roll Number"] = "R12345"

print(marksheet)
print("---------------------------------")

marksheet["Roll Number"] = "R78902"

marksheet["Marks"] = [23,34,45,56,67]

marksheet["Marks2"] = {"Maths" : 23 ,
                       "English" : 45,
                       "Physics":78,
                       "Biology" : 67,
                       "Chemistry":50}

print(marksheet)
print("---------------------------------")

print(marksheet.popitem())
print("---------------------------------")
print(marksheet)

print("---------------------------------")
print(marksheet.pop("Name"))
print("---------------------------------")
print(marksheet)

print("---------------------------------")
marksheet.clear()
print(marksheet)
