# Takiong integer input from
n = int(input("Enter any number: "))
sum1 = 0   # this will be used to add divisble numbers

# checking if it is perfect number
if n > 0:   # Makeing sure number is positive
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")
else :
    print("Only positve integers can be perfect number.")
