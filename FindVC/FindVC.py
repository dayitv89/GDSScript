import sys
from os import walk 
from pprint import pprint
from ioshooker import *

files = []
dirs = [sys.argv[1]]

def listAll(path, ext):
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend([path+'/'+f for f in filenames if f.endswith(ext)])
        dirs.extend([path+'/'+f for f in dirnames])
        break

def parseHeader(filePath, outputFileName = "out.txt"):
	try:
	    objc = ObjcHeader(filePath, outputFileName)
	    print objc.class_name + " : " + objc.super_class_name
	except ValueError as error:
	    pass

### finds all directories recursively into `dirs`; and finds only .h files into `files`
for a in dirs: listAll(a, ".h") 

# pprint(files)
for fl in files: parseHeader(fl)






