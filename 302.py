import math

a = int(input())
b = int(input())
c = int(input())

if a < b:
    gip = b
    cat1 = a
    cat2 = c
    if c > b:
        gip = c
        cat1 = a
        cat2 = b

else:
    gip = a
    cat1 = b
    cat2 = c
    if c > a:
        gip = c
        cat1 = a
        cat2 = b

gp = math.hypot(cat1, cat2)

if gip < cat1 + cat2:
    if gip == gp:
        print('right')
    elif gip > gp:
        print('obtuse')
    elif gip < gp:
        print('acute')
else:
    print('impossible')
