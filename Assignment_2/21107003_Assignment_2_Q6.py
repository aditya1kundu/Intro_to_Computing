a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = (a^b)
d = bin(c)
count = 0
for i in d[2:]:
    if i == "1":
        count += 1
        print(count)
