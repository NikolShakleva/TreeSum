import sys

def foursum(vals):
    N=len(vals)
    P = dict()
    for i in range(N):
        P[+vals[i]] = i

    for j in range(N):
        for i in range(j):
            # if P.get(-vals[i]-vals[j],0) > j:
                return True
    return False

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    vals = list(map(int, sys.stdin.readlines()))
    print("Found" if foursum(vals[:N]) else "None")
