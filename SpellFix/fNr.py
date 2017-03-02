
import sys
from os import walk
from spellCheck import *

keywords = [f.rstrip().lower() for f in open('keywords.txt', 'r')]
print keywords

def printDetails(filePath):
    print filePath
    val = ''
    lineNo = 0
    val = "\n\n=============================================================\n"
    val += filePath
    val += "\n--------------------------------------------------------------\n"
    for line in open(filePath, 'r'):
        lineNo += 1
        lines = re.findall('[a-z]+', line.lower())
        for word in lines:
            word = word.rstrip().lower()
            if word in keywords: continue
            a = correct(word)
            if a != word:
                wordChange = 'Line: '+str(lineNo)+' => '+word+' != '+a+'\n'
                val += wordChange
                print wordChange
    val += "\n\n----------------------------------------------------------\n\n"
    file_op = open(filePath+".gds.txt", "w")
    file_op.write(val)
    file_op.close()

files = []
dirs = [sys.argv[1]]

def listAll(path):
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend([path+'/'+f for f in filenames if not f.startswith('.')])
        dirs.extend([path+'/'+f for f in dirnames])
        break

for a in dirs: listAll(a)
for fl in files: printDetails(fl)
