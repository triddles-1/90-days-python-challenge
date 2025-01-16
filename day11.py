import re
#take input from the user
email = input("Please type a legit email address:   ")
#Assign a Regex
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|mail|org|site|me)"
#test the condition if it's true
if re.search(pattern, email):
    print("Good, This is a valid email")
else:
    print("Naah, This is not a valid email, try again")
    
    