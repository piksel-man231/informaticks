i0 = int(input())
pm = 1
maks = 1
while i0 != 0:
    i1 = int(input())
    if i1 == i0:
        pm = pm + 1
    else:
        pm = 1
    if pm > maks:
        maks = pm
    i0 = i1
print (maks)