# this is python3
import sys,random,subprocess,statistics,platform
from timeit import default_timer as timer

from pathlib import Path

python=sys.executable
if '' == python:
    python = 'python3'
# you may need to overwrite this in certain situations
java="java"
javac="javac"

# compilation on init (object creation)
# all filenames are Path()
class Process:
    def __init__(self,sourcefile,nickname = ''):
        self.sourcefile = Path(sourcefile)
        self.nickname = self.sourcefile.stem if nickname == '' else nickname
    def __repr__(self):
        return "Process " + self.sourcefile.as_posix()

class JavaProcess(Process):
    def __init__(self, sourcefile, nickname = '',parameters=[]):
        super().__init__(sourcefile,nickname=nickname)
        self.classpath = self.sourcefile.parent.as_posix()
        self.classfile = self.sourcefile.with_suffix('.class')
        # print(self.classfile)
        if (not self.classfile.exists()) or self.sourcefile.stat().st_mtime > self.classfile.stat().st_mtime:
            print('compile {}'.format([javac, '-cp',self.classpath, self.sourcefile.as_posix()]))
            subprocess.run([javac, '-cp',self.classpath, self.sourcefile.as_posix()],check=True)
        self.aslist=[java, '-cp', self.classpath,
                self.sourcefile.stem] + parameters

class PythonProcess(Process):
    def __init__(self, sourcefile,nickname=''):
        super().__init__(sourcefile,nickname=nickname)
        self.aslist=[python, sourcefile]

class RustProcess(Process):
    def __init__(self, source, nickname = '',parameters=[]):
        super().__init__(Path(source)/'src/main.rs',nickname=nickname)
        self.executable = Path("{0}/target/release/{0}".format(source))
        print(self.sourcefile,self.executable)
        if (not self.executable.exists()) or self.sourcefile.stat().st_mtime > self.executable.stat().st_mtime:
            print('compile {}'.format([self.sourcefile.as_posix(),self.executable.as_posix()]))
            subprocess.run(['cargo', 'build','--release'],cwd=source,check=True)
        self.aslist=[self.executable]+parameters

results = dict()
def runExp(producer,tested,tableDir, Nlist=[100],seed = 0, results = results,timelimit = 5, hardtimelimit = 30 ):
    FastCmp = dict()
    for N in Nlist:
        FastCmp[N]=[]
    for i in range(4):
        myseed = seed + 7896*i
        extra = [ str(myseed) ] if seed > 0 else []
        table_file = tableDir / Path(producer.nickname + tested.nickname+ '.table')
        for N in Nlist:
            prodtuple = tuple( producer.aslist + [str(N)] + extra)
            shelltext = " ".join(prodtuple) +" | " +" ".join(tested.aslist)
            print( shelltext)
            try:
                start = timer()
                ps = subprocess.Popen(prodtuple, stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
                result = subprocess.run(tested.aslist, stdin=ps.stdout,stderr=subprocess.PIPE,stdout=subprocess.PIPE,check=True, timeout=hardtimelimit)
                ps.wait()
                end = timer()
            except subprocess.TimeoutExpired:
                break

            measure = end-start
            FastCmp[N].append(measure)
            print("Time: " + str(measure)   )
            if seed > 0:
                outp = result.stdout.decode("utf-8").strip()
                if (N,myseed) in results  and not results[(N,myseed)][0] == outp:
                    print("different results for N={} seed={} tested={}: is='{}' (err: '{}'), should be '{}'".format(N,myseed,tested,outp,result.stderr.decode("utf-8").strip(),results[(N,myseed)]))
                    exit(1)
                else:
                    results[(N,myseed)] = (outp,shelltext)
            #        print('Output: ' + output.decode("utf-8") )
            if measure > timelimit:
                break

    if table_file == '':
        table = sys.stdout
    else:
        table = table_file.open('w')

    for N in sorted(FastCmp.keys()):
        mm = FastCmp[N]
        if len(mm) > 0: ## mean and stddev are somewhat arbitrary - we'll get back to this later in the course
            mean = statistics.mean(mm) 
            stddev = statistics.stdev(mm) if len(mm) > 1 else 0 
            print("{:4} {:.3f} {:.3f}".format(N,mean,stddev),file=table)
    table.close()

def prepareTableDir():
    githash = subprocess.check_output(["git","rev-parse","--short","HEAD"]).decode("utf-8")[:-1]
    nodename = platform.node()

    TableDir="./Tables-{}-{}".format(nodename,githash)
    i=1
    while Path(TableDir).exists():
        TableDir="./Tables{}-{}-{:02}".format(githash,nodename,i)
        i += 1
    testdir = Path(TableDir)
    testdir.mkdir() # force it to be empty - parents=True, exist_ok=True)
    if len(subprocess.check_output(["git","status","--porcelain"])) > 0:
        subprocess.run("cd {0}; git status --porcelain > gitst.txt; git diff > patch.diff".format(TableDir),shell=True)

    subprocess.run("cd {}; ({} --version; {} -version;{} -version) > versions.txt".format(TableDir,python,javac,java),shell=True)

    with (testdir / 'platform.txt').open('w') as pf:
        print(platform.platform(), file=pf)
        print(platform.processor(), file=pf)
    return testdir
