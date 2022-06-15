# Python code to count the number of occurrences of each word in the list

a= ['digvijay','aditya','pulkit','vriti','vriti','saksham','kundu','digvijay']
print(f"\nThe list is : {a}\n")

for i in a:
    g = 0
    n = 0
    if(i=='----'):
        continue

    for j in a:
        if(i == j):
            n += 1
            a[g] = '----'
        g += 1
    print(f"{i} occured {n} times")
