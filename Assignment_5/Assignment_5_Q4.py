# Python code to print given pattern of '*'

# Printing * in ascending order
for i in range(1,6) :   # to put numbers 1 to 6 in j's range
    for j in range(0,i) :   # to print * according to i's value
        print('*', end='')
    print()

# Printing * in descending order
for i in range(0,5):
    j=4-i
    while(j>0):
        print('*', end='')
        j=j-1
    print()
