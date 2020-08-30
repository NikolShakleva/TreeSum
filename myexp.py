import APAexp

import sys,random,subprocess,statistics,pathlib,platform

from APAexp import Process,JavaProcess,PythonProcess, runExp, prepareTableDir


python='python3'
java="java"
javac="javac"

Nlist = [int(90*1.41**i) for i in range(20)]
print(Nlist)

timelimit = 10     # in seconds; if we exceed this, we don't try anything bigger
hardtimelimit = 100 # then the OS is going to kill it -- protection agains infinite loops and alike

TableDir = prepareTableDir()

weed=JavaProcess('Weed.java') ## supplying only 

testlist = [
    JavaProcess("javaSol/Simple.java",    nickname='JavaSimple'),
    JavaProcess("javaSol/HashPairs.java", nickname='JavaDict'),
    PythonProcess('pythonSol/simple.py',  nickname='PythSimple'),
    PythonProcess('pythonSol/fastDict.py',nickname='PythDict')
]
for pp in testlist:
    runExp(weed,pp,TableDir, Nlist=Nlist,seed=12345,timelimit = timelimit,hardtimelimit=hardtimelimit)

