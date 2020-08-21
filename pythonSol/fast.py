from __future__ import print_function
import sys, bisect

N = int(sys.stdin.readline())
vals = list(map(int, sys.stdin.readlines()))

L, M = [],[]

for i in range(0, N):
    for j in range(i+1, N):
        L.append((+vals[i]+vals[j], i,j))
        L.append((-vals[i]-vals[j], i,j))

L.sort()

for q in range(len(L)-1):
    x, i,j = L[q]
    p=q+1
    while p < len(L) and L[p][0] == x: 
        y, k,l = L[p]
        p+=1
        if j < k and vals[i]+vals[j]+vals[k]+vals[l] == 0:
            print(i,j,k,l,file=sys.stderr)
            print(True)
            sys.exit()
print(False)
