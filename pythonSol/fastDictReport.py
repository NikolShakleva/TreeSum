import sys

def foursum(vals,report=False):
    N=len(vals)
    P = dict()
    for j in range(N):
        for i in range(j):
            if +vals[i]+vals[j] not in P:
                P[+vals[i]+vals[j]] = j

    for j in range(N):
        for i in range(j):
            if -vals[i]-vals[j] in P and P[-vals[i]-vals[j]] <i:
                jj = P[-vals[i]-vals[j]]
                for ii in range(jj): 
                    if vals[ii]+vals[jj]+vals[i]+vals[j] == 0:
                        if report:
                            print(ii,jj,i,j,file=sys.stderr)
                        return True
    return False

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    vals = list(map(int, sys.stdin.readlines()))
    print(foursum(vals[:N],report=True))
