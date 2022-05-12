# Taking input
string= str(input("Enter any string: "))

# Using string slicing to find a word in the string
checked = string.find("name")

# Making a loop for printing yes and no for the required outputs.
# Here '==' is comparison operator
if checked == -1:     # '-1' is the value as an output of find function indicating the absence of particular string in it.
    print("No")
    
else:
    print("Yes")
