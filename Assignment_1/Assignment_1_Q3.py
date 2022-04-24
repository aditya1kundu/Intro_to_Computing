# Code to input the number the seconds
seconds = int(input("Enter the number of seconds to be converted: "))

# Code to calculate and print number of seconds and minutes
#For minutes
minutes = seconds // 60     #floor division operator is used
#For remaining seconds
remaining_seconds = seconds % 60   #Modulus operator is used
print("Minutes :" , minutes)
print("Seconds :" , remaining_seconds)
