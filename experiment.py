# this is python3
import sys,random,subprocess,statistics,pathlib
from timeit import default_timer as timer

# looping with outermost loop in the repetition of the experiment would be even better

python='python3'
Nlist = [int(30*1.41**i) for i in range(23)]

print(Nlist)

TableDir="./Tables"

pathlib.Path(TableDir).mkdir() # force it to be empty - parents=True, exist_ok=True)

subprocess.run("javac Weed.java",shell=True,check=True)
weed=('java', '-cp', '.','Weed')
subprocess.run("javac javaSol/Simple.java",shell=True,check=True)
simpJava=('java', '-cp', 'javaSol','Simple')
subprocess.run("javac javaSol/HashPairs.java",shell=True,check=True)
dictJava=('java', '-cp', 'javaSol','HashPairs')

simpPyth=(python, 'pythonSol/simple.py')
dictPyth=(python, 'pythonSol/fastDict.py')

def prodExp(prod,name,seed=0):
    runExp(prod,simpJava,tableFile=TableDir+'/'+name+'JavaSimple.table', Nlist=Nlist,seed=seed)
    runExp(prod,simpPyth,tableFile=TableDir+'/'+name+'PythSimple.table', Nlist=Nlist,seed=seed)
    runExp(prod,dictJava,tableFile=TableDir+'/'+name+'JavaDict.table',   Nlist=Nlist,seed=seed)
    runExp(prod,dictPyth,tableFile=TableDir+'/'+name+'PythDict.table',   Nlist=Nlist,seed=seed)

def _main():
    prodExp(weed,"Weed",seed = 12345)

results = dict()
def runExp(producer,tested,tableFile='', Nlist=[100],seed = 0, results = results ):
    FastCmp = dict()
    for N in Nlist:
        FastCmp[N]=[]
    for i in range(4):
        myseed = seed + 7896*i
        extra = [ str(myseed) ] if seed > 0 else []
        for N in Nlist:
            print( tableFile, tuple( list(producer) + [str(N)] +extra) )
            try:
                start = timer()
                ps = subprocess.Popen(tuple( list(producer) + [str(N)] + extra), stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
                result = subprocess.run(tested, stdin=ps.stdout,stderr=subprocess.PIPE,stdout=subprocess.PIPE,check=True, timeout=30)
                ps.wait()
                end = timer()
            except subprocess.TimeoutExpired as e:
                break

            measure = end-start
            FastCmp[N].append(measure)
            print("Time: " + str(measure)   )
            if seed > 0:
                outp = result.stdout.decode("utf-8")
                if (N,myseed) in results  and not results[(N,myseed)] == outp:
                    print("different results for N={} seed={} tested={}: is={} ({}), should be {}".format(
                        N,myseed,tested,outp,result.stderr.decode("utf-8"),results[(N,myseed)]))
                    exit(1)
                else:
                    results[(N,myseed)] = outp
            #        print('Output: ' + output.decode("utf-8") )

    if tableFile == '':
        table = sys.stdout
    else:
        table = open(tableFile,'w')

    for N in sorted(FastCmp.keys()):
        mm = FastCmp[N]
        if len(mm) > 0:
            mean = statistics.mean(mm) 
            stddev = statistics.stdev(mm) if len(mm) > 1 else 0
            print("{:4} {:.3f} {:.3f}".format(N,mean,stddev),file=table)

if __name__ == '__main__':
    _main()
