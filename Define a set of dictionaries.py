#Define a set of dictionaries
dict1 = {"apple": 10, "banana": 20, "cherry": 30}
dict2 = {"dog": 5, "cat": 8, "elephant": 15}
dict3 = {"car": 100, "bike": 50, "plane": 200}

#Combine all dictionaries into a list (or set of dictionaries)
dicts = [dict1, dict2, dict3]

#Ask for user input
user_input = input("Enter a key to search: ")

#Search for the key in all dictionaries
found = False
for d in dicts:
    if user_input in d:
        print(f"The value for '{user_input}' is: {d[user_input]}")
        found = True
        break

if not found:
    print(f"Key '{user_input}' not found in any dictionary.")

