

files = []
dirs = [sys.argv[1]]
def listAll(mypath):
    for (dirpath, dirnames, filenames) in walk(mypath):
        files.extend([mypath+f for f in filenames if not f.startswith('.')])
        dirs.extend([mypath+'/'+f for f in dirnames])
        break

for a in dirs:
    listAll(a)

print len(files)
