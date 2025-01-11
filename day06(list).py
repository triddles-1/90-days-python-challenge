#a pregram that takes user input and prints sum and average
user_input =input("Enter your numbers separateed by spaces:  ").split()
# Convert each item in the list to an integer
user_input = [int(x) for x in user_input]
print(f"The numbers you typed was {user_input}")
#print sum
user_sum = sum(user_input)
print(f"The sum of the numbers you typed was: {user_sum}")
#print average
user_avg = sum(user_input) / len(user_input)
print(f"The Average of the numbers you typed was: {user_avg}")

