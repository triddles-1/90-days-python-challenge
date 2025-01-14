#create a program that handles error and prints out the error

try:
    num = int(input("Type any number you want:  "))
    print(num)
except ValueError:
    print("Please Enter an Integer")
    