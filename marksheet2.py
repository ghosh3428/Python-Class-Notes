marksheet = dict()

marksheet["Name"] = "Rohan Mishra"
marksheet["Roll Number"] = "R12345"
marksheet["Marks"] = [23,34,45,56,67]

print(marksheet)

print("----------------------------------------------")
print(marksheet.values())

print("----------------------------------------------")
print(marksheet.keys())

print("----------------------------------------------")
print(marksheet.items())

print("----------------------------------------------")
print("Name :",marksheet["Name"])

print("----------------------------------------------")
print("Name :",marksheet.get("Name"))

