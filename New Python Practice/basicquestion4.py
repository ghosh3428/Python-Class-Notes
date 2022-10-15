#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
word=str(input("enter a word:"))
if word.find("is") == 0:
    print(word)
else:
    print("is"+word)
