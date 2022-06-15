# Python code to calculate area of triangle using Heron's formula

import math    # math module for finding square root
side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

# this is heron's formula for area of triangle
s = ( side1 + side2 + side3 )/2
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))

print(f'Area of the triangle: {area}')
