#Assign two mathematical operation to different varibles.
#the outcome of two varibles must be equall.
import random
a, b, c = [5.0, 7.0, 1.0]
k = [1.0, 2.0, 3.0, 4.0, 5.0]
m = random.choice(k)
V1 = a + c
V2 = b - c
if V1 == V2:
    print( V1, V2)
    while True:
        m = random.choice(k)
        V3 = m + m
        V4 = m * m
        if V3 == V4:
            break
print(V3, V4)
        
    
