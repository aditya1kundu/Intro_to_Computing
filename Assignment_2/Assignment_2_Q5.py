# Taking inputs of the sides of the triangle.
s1 = int(input("Enter First length : "))
s2 = int(input("Enter Second length : "))
s3 = int(input("Enter Third length : "))

# Checking the condition for triangle to be formed.
C1 = s1 > s2 + s3
C2 = s2 > s1 + s3
C3 = s3 > s1 + s2

# Here we check wheather the all conditions are satisfied or not.
Output = str(C1 or C2 or C3)

print("The triangle can be formed?")

# Using string slicing.
print(Output.replace("True", "No!").replace("False", "Yes!"))
