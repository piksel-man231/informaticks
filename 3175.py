N, K = input().split()
# print(K)
# print(N)
aa = []

N = int(N)
K = int(K)

for i in range(1, N+1):
    aa.append('I')

for m in range(1, K+1):
    a1, a2 = input().split()
    a1 = int(a1)
    a2 = int(a2)
    for j in range(a1, a2+1):
        aa.pop(j-1)
        #print(aa)
        aa.insert(j-1, '.')
        #print(aa)
        #print(' ')
print(''.join(aa))
