#Define a set of dictionaries
dicts = {"jose": 10, "messi": 20, "jay": 30}


#Ask for user input
user_input = input("Enter a key to search: ")

#Search for the key in all dictionaries
found = False
for key, value in dicts.items():
    if user_input == key:
        print(f"The value for '{user_input}' is: {value}")
        found = True
        break

if not found:
    print(f"Key '{user_input}' not found in any dictionary.")
