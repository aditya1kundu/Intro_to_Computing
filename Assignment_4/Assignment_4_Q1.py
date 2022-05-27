print("\nGrading system of a school!")

#taking input from user
marks = int(input("Enter your marks obtained( out of 100): "))

#if-elif loop is used here to print grade according to marks obtained.
if marks < 25:
    print("Your Grade is: F")
elif 25 <= marks <= 45:
    print("Your Grade is: E")
elif 45 < marks <= 50:
    print("Your Grade is: D")
elif 50 < marks <= 60:
    print("Your Grade is: C")
elif 60 < marks <= 80:
    print("Your Grade is: B")
elif 80 < marks < 100:
    print("Your Grade is: A")
