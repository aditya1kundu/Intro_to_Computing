# Python code to find the number divisible by 7 and 11 between [1,500)

for num in range (1,500):
    
    # checking for divisibility
    if (num % 7 == 0 and num % 11 == 0):
        print(num)
