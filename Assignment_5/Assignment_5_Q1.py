# Python code to reverse a string

string = "My name is Aditya"
length = len(string)

print(f"This is the string: '{string}'")
print(f"This is the length of string: {length}")
print("Reverse of the string is: ", end ='')

# Using while loop to print from the end
while length > 0:
    # using length to define which index to print first, as index start from 0
    print( string[length - 1], end='' )
    length -= 1
