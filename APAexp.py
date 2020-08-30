# this is python3
import sys,random,subprocess,statistics,platform

from pathlib import Path

python='python3'
java="java"
javac="javac"

# compilation on init (object creation)
# all filenames are Path()
class Process:
    def __init__(self,sourcefile):
        self.sourcefile = Path(sourcefile)
    def __repr__(self):
        return "Process " + self.sourcefile.as_posix()

class JavaProcess(Process):
    def __init__(self, sourcefile):
        super().__init__(sourcefile)
        self.classpath = self.sourcefile.parent.as_posix()
        self.classfile = self.sourcefile.with_suffix('.class')
        # print(self.classfile)
        if self.sourcefile.stat().st_mtime > self.classfile.stat().st_mtime:
            print('compile {}'.format([javac, '-cp',self.classpath, self.sourcefile.as_posix()]))
            subprocess.run([javac, '-cp',self.classpath, self.sourcefile.as_posix()],check=True)
        self.aslist=[java, '-cp', self.classpath,self.sourcefile.stem]

class PythonProcess(Process):
    def __init__(self, sourcefile):
        super().__init__(sourcefile)
        self.aslist=[python, sourcefile]
