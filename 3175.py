N, K = (K for K in input() if K != ' ')
a = []

for i in range(1, N):
    a.append('I')

for m in range(1, K):
    a1, a2 = (a2 for a2 in input() if a2 != ' ')
    for j in range(a1, a2):
        a[j] = '.'

print(a)
