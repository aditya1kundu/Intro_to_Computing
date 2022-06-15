# Python code to print a triangular pattern of alphabet

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input("Enter the number: "))
for i in range( 1, n+1 ):   # Increasing n by 1 as range dosn't include upperlimit
    if len(a) < i:
        a += 1
    for j in range(0,i):
        print(a[j], end='')

    print()

    a = a[i:]
print("\n")
