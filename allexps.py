from APAexp import Process,JavaProcess,PythonProcess, runExp, prepareTableDir

stressP = [ JavaProcess("Produce.java",parameters=["plant"],nickname='PrdPt'),
            JavaProcess("Produce.java",parameters=["no"],nickname='PrdNo')]
testlist = [
    JavaProcess("javaSol/Simple.java",    nickname='JavaSimple'),
    JavaProcess("javaSol/HashPairs.java", nickname='JavaDict'),
    PythonProcess('pythonSol/simple.py',  nickname='PythSimple'),
    PythonProcess('pythonSol/fastDict.py',nickname='PythDict')
]

TableDir = prepareTableDir()

# stresstest, aiming at correctness
stressListN = [10,50] 
for seed in [5679]: # runExp does 3 runs with modified seed, add more seeds here if needed
    for prodProc in stressP:
        resDict = dict()
        for testProc in testlist:
            print(seed,prodProc.nickname,testProc.nickname)
            runExp(prodProc,testProc,TableDir,results=resDict, 
                    Nlist=stressListN,seed=seed)

# now the performance tests
Nlist = [int(90*1.41**i) for i in range(2)]
print("-"*80)
print(Nlist)
timelimit = 10     # in seconds; if we exceed this, we don't try anything bigger
hardtimelimit = 100 # then the OS is going to kill it -- protection agains infinite loops and alike
weed=JavaProcess('Weed.java') ## supplying only 
for pp in testlist:
    runExp(weed,pp,TableDir, Nlist=Nlist,seed=12345,timelimit = timelimit,hardtimelimit=hardtimelimit)
