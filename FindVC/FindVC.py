import sys
from os import walk 
from pprint import pprint

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
    # print filePath
    val = ''
    lineNo = 0
    # val = "\n\n=============================================================\n"
    # val += filePath
    sep = 0
    # val += "\n--------------------------------------------------------------\n"
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
        # for word in lines:
            # word = word.rstrip().lower()
            # if word in keywords: continue
            # a = correct(word)
            # if a != word:
            #     wordChange = 'Line: '+str(lineNo)+' => '+word+' != '+a+'\n'
            #     val += wordChange
            #     print wordChange
    # val += "\n\n----------------------------------------------------------\n\n"
    print val
    # file_op = open(filePath+".gds.txt", "w")
    # file_op.write(val)
    # file_op.close()

# finds all directories recursively into `dirs`; and finds only .h files into `files`
for a in dirs: listAll(a, ".h") 

# pprint(files)
for fl in files: printDetails(fl)