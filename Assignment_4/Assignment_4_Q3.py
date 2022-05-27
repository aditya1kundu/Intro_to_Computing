import random

print("\nMultiplication Game","\nThere will be 10 questions.","\n\nStarting...")

# Number of trials of game
i=1
while i <=10:       # Loop will continue till 10th trial of question
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    print("Question-",i,":", x, "*", y)
    r = int(input("Enter your result:")) # r is the result to be entered by user
    if r == x*y:
        print("Right!")
    else:
        print("Wrong!", "The correct answer is:", x*y)
    i+= 1
