from __future__ import print_function
import sys, bisect

N = int(sys.stdin.readline())
vals = list(map(int, sys.stdin.readlines()))

L=[]

for i in range(0, N):
    for j in range(i+1, N):
        L.append((+vals[i]+vals[j], j))

L.sort()

V=[]
J=[]
c=L[0][0]-1
for (v,j) in L:
    if v != c:
        V.append(v)
        J.append(j)
        c=v

n=len(V)
for i in range(0, N):
    for j in range(i+1, N):
        v=-vals[i]-vals[j]
        b=bisect.bisect_left(V,v)
        if b<n and v==V[b] and J[b] < i:
            print(True)
            sys.exit()
print(False)
