import sys

def foursum(vals):
    N=len(vals)
    P = dict()
    for i in range(N):
        for j in range(i+1,N):
            P[+vals[i]+vals[j]] = i

    for j in range(N):
        for i in range(j):
            if P.get(-vals[i]-vals[j],0) > j:
                return True
    return False

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    vals = list(map(int, sys.stdin.readlines()))
    print(foursum(vals[:N]))
