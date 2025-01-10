#write a function that takes any number and return it's factorial
#declare function
def factorial(num):
    factorial=1
    for i in range(1, num + 1):
        factorial *= i
    print(f"the factorial of the number '{num}' is {factorial}")

#print the function
print(factorial(int(input("type in any number:   "))))
