# Python code to find odd, even, positive, negative and occurence of each numbers
# in the entered 10 numbers

# creating an empty list
numbs = []

print("Enter 10 Elements to add in a list")
n = 10

# iterating till the range
for i in range(0, n):
    elements = int(input())

    numbs.append(elements) # adding the element to the empty list

print(f"Entered list is: {numbs}")

# Checking for positive numbers
print("Positive numbers in List are: ")
for i in numbs:
    if i > 0:
       print(i, end = "")
print("\n")

# Checking for negative numbers
print("Negative numbers in List are: ")
for i in numbs:
    if i < 0:
        print("\n")
        print(i, end = "")
print("\n")

# Checking for Odd numbers
print("Odd numbers in List are: ")
for i in numbs:
    if i % 2 != 0:
       print(i, end = "")
print("\n")

# Checking for even numbers
print("Even numbers in List are: ")
for i in numbs:
    if i % 2 == 0:
       print(i, end = "")

print("\n")
# Finding Occurence of each number
print('Occurence of each number is: ')
for i in numbs:
    if(type(i) == float):   # so no repetition occurs
        continue
    n=0
    j=0
    while j<10:
        if(numbs[j]==i):
            n=n+1
            numbs[j]=1.1   # an decimal no which would be used afterwards to distinguish it from others
        j=j+1
    print(f"Frequency of {i} is : {n}")
print("\n")
