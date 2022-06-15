# Python code to find numbers divisible by a specific number in a range.

lower_range = int(input("Enter the lower range...."))
upper_range = int(input("Enter the upper range...."))
div_num = int(input("enter the number to be divisible by...."))

i = lower_range + 1    # so that starting and ending numeber are not considered
while i < upper_range:
    # if remainder is zero that means particular number is divisible by given number
    if ( i % div_num == 0 ):
        print(i)
    i = i + 1
