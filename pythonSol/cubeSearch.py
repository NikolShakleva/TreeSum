from __future__ import print_function
import sys, bisect

N = int(sys.stdin.readline())
V = list(map(int, sys.stdin.readlines()))

V.sort()

n=len(V)
for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            v=-V[i]-V[j]-V[k]
            b=bisect.bisect_left(V,v)
            if b<n and v==V[b] and b < i:
                print(True)
                sys.exit()
print(False)
