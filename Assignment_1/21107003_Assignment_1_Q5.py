import math     #Importing maths modules in order to use sine and cosine function.
a = 0
while a <= 345 :      #making a loop each of 15 degree angle.
    sin_a = math.sin(math.radians(a))
    cos_a = math.cos(math.radians(a))
    print(str(a) + " --- " + str(round(sin_a , 4)) + " , " + str(round(cos_a , 4)))
    a += 15
