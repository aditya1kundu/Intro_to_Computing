
def pangram(str):
    All_alphabets = "abcdefghijklmnopqrstuvwxyz"
    for i in All_alphabets:
        if i not in str.lower():   # As python is case sensitive, so we have to check its small letters too
            return False

    return True

# Example:
string = input("Enter the sentence: ")
if(pangram(string) == True):
    print("Yes, The given string is pangram.")
else:
    print("No, the given string is not a pangram.")
