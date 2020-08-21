import sys

def foursum(vals,report=False):
    N=len(vals)
    P = dict()
    for j in range(N):
        for i in range(j):
            if +vals[i]+vals[j] not in P:
                P[+vals[i]+vals[j]] = (i,j)

    for k in range(N):
        for l in range(k):
            if -vals[k]-vals[l] in P:
                (i,j) = P[-vals[k]-vals[l]]
                if j < k and vals[i]+vals[j]+vals[k]+vals[l] == 0:
                        if report:
                            print(i,j,k,l,file=sys.stderr)
                        return True
    return False

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    vals = list(map(int, sys.stdin.readlines()))
    print(foursum(vals[:N],report=True))
