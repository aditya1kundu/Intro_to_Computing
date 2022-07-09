# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]


# taking input
print("Kindly enter alphabets only.")
s = input("Enter word/sentence to be checked: ").replace(" ","").lower()
ans = isPalindrome(s)   # calling function

# checking palindrom
if ans:
    print("Yes")
else:
    print("No")
