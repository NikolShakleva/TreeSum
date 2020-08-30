# this is python3
import sys,random,subprocess,statistics,pathlib,platform
from timeit import default_timer as timer



python='python3'
java="java"
javac="javac"

Nlist = [int(30*1.41**i) for i in range(29)]
print(Nlist)

timelimit = 5      # in seconds; if we exceed this, we don't try anything bigger
hardtimelimit = 100 # then the OS is going to kill it -- protection agains infinite loops and alike

def _main():
    td = prepareTableDir()
    prodExp(weed,"Weed",seed = 12345,tabledir = td)

def prepareTableDir():
    githash = subprocess.check_output(["git","rev-parse","--short","HEAD"]).decode("utf-8")[:-1]
    nodename = platform.node()

    TableDir="./Tables-{}-{}".format(nodename,githash)
    i=1
    while pathlib.Path(TableDir).exists():
        TableDir="./Tables{}-{}-{:02}".format(githash,nodename,i)
        i += 1
    testdir = pathlib.Path(TableDir)
    testdir.mkdir() # force it to be empty - parents=True, exist_ok=True)
    if len(subprocess.check_output(["git","status","--porcelain"])) > 0:
        subprocess.run("cd {0}; git status --porcelain > gitst.txt; git diff > patch.diff".format(TableDir),shell=True)

    subprocess.run("cd {}; ({} --version; {} -version;{} -version) > versions.txt".format(TableDir,python,javac,java),shell=True)

    with (testdir / 'platform.txt').open('w') as pf:
        print(platform.platform(), file=pf)
        print(platform.processor(), file=pf)

subprocess.run([javac, "Weed.java"],check=True)
weed=(java, '-cp', '.','Weed') ## supplying only 
subprocess.run([javac, "javaSol/Simple.java"],check=True)
simpJava=(java, '-cp', 'javaSol','Simple')
subprocess.run([javac, "javaSol/HashPairs.java"],check=True)
dictJava=(java, '-cp', 'javaSol','HashPairs')

simpPyth=(python, 'pythonSol/simple.py')
dictPyth=(python, 'pythonSol/fastDict.py')

def prodExp(prod,name,seed=0):
    runExp(prod,simpJava,tableFile=TableDir+'/'+name+'JavaSimple.table', Nlist=Nlist,seed=seed)
    runExp(prod,simpPyth,tableFile=TableDir+'/'+name+'PythSimple.table', Nlist=Nlist,seed=seed)
    runExp(prod,dictJava,tableFile=TableDir+'/'+name+'JavaDict.table',   Nlist=Nlist,seed=seed)
    runExp(prod,dictPyth,tableFile=TableDir+'/'+name+'PythDict.table',   Nlist=Nlist,seed=seed)

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
                result = subprocess.run(tested, stdin=ps.stdout,stderr=subprocess.PIPE,stdout=subprocess.PIPE,check=True, timeout=hardtimelimit)
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
            if measure > timelimit:
                break

    if tableFile == '':
        table = sys.stdout
    else:
        table = open(tableFile,'w')

    for N in sorted(FastCmp.keys()):
        mm = FastCmp[N]
        if len(mm) > 0: ## mean and stddev are somewhat arbitrary - we'll get back to this later in the course
            mean = statistics.mean(mm) 
            stddev = statistics.stdev(mm) if len(mm) > 1 else 0 
            print("{:4} {:.3f} {:.3f}".format(N,mean,stddev),file=table)

if __name__ == '__main__':
    _main()
