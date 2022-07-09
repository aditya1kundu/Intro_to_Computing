# Print Pascal's Triangle in Python
from math import factorial

r = int(input("Enter the number of rows: "))    # r for rows
for i in range(r):
    for j in range(r-i+1):

        # for left spacing
        print(end=" ")

    for j in range(i+1):

        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

    # for new line
    print()
