# Python code to print prime number for a user input range

# Taking range from user
lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))

for i in range(lower_range,upper_range):
    flag = 0
    for j in range(2,i):
        if(i % j == 0):
            flag = 1
            break
    if(flag == 0):
        print(i)
