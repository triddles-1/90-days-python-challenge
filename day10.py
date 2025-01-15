# A PYTHON SCRIPT THAT CALCULATES THE SUARE ROOT OF A NUMBR USING THE MATH LIBRARY
import math
from math import sqrt
number = int(input("enter any number you like:  "))
square = sqrt(number)
if square.is_integer():
    print(f"The square root of the number {number} is {int(square)}")
else:
    print(f"The square root of the number {number} is {square}")
