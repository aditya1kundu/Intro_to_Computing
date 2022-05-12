'''For taking length of string
First take input of string'''

string = "Python is a case sensitive language"

#len() is used for taking length of given string.
print("A) Length of the given string: ",len(string),"\n") 

# This is for giving output string in reverse order.
print("B) Reverse of the given string is :")
print(string[::-1],"\n")    

#slicing the string.
new_string = string[10:26]
print("C) New sliced string is: ","\n", new_string,"\n")

#replace a string using replace fun. in string slicing,
Replaced_string= string.replace('a case sensitive' , 'object oriented')
print("D) String after replacing: ", "\n" ,Replaced_string ,"\n")

#Finding the index of "a" in the input string.
print("E) Index of substring 'a' is:", string.find("a"),"\n")

#Printing the string without white spaces using replace in string.
print("F) Sting without white spaces: ","\n",string.replace(" ", ""))

