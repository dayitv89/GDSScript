import sys
from os import walk 
from pprint import pprint
from ioshooker import *

files = []
dirs = [sys.argv[1]]

linesExcept = ("//", "#")
lineInclude = ("@interface")

def listAll(path, ext):
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend([path+'/'+f for f in filenames if f.endswith(ext)])
        dirs.extend([path+'/'+f for f in dirnames])
        break

def printDetails(filePath):
    val = ''
    lineNo = 0
    sep = 0
    for line in open(filePath, 'r'):
    	line = line.strip()
    	if line.startswith(linesExcept): continue
        lineNo += 1
        if line.startswith("@interface"):
        	if sep == 0:
        		val += "\n\n--------------------------------------------------------------\n"
        		val += filePath
        		val += "\n--------------------------------------------------------------\n"
        		sep = 1
        	val += 'Line: '+str(lineNo)+' => '+line+'\n'
    if sep == 1: val += "\n--------------------------------------------------------------\n"
    print val
    

### finds all directories recursively into `dirs`; and finds only .h files into `files`
for a in dirs: listAll(a, ".h") 

# pprint(files)
for fl in files: printDetails(fl)






