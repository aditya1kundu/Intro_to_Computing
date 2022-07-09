
class validation:
   def is_valid_parenthese(self, str1):
        #Here two datatypes are used such as list and dictionary providing a key value pairs.
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        #Using for loop we will check the desired keys and add them in stack.
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            #If not in pchar, we will pop that parantheses!!!
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

# we call the function here!
print(validation().is_valid_parenthese("(){}[]"))
print(validation().is_valid_parenthese("()"))
print(validation().is_valid_parenthese("[)"))
print(validation().is_valid_parenthese("({[)]"))
print(validation().is_valid_parenthese("{{{"))
