#
# find all files in the directory recursive and list up with the whole name
### RUN $ python find_all.py /Users/gds/Desktop/Projects
# It will show you the terminal JSON output;
### wanna to save it to file? RUN $ python find_all.py /Users/gds/Desktop/Projects > data.json
# and it will create data.json file and write all the data.
#
# Writer : GauravDS
#

import sys
from os import walk
import json

files = []
dir = [sys.argv[1]]

def listAll(path):
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend([path+'/'+f for f in filenames if not f.startswith('.')])
        dir.extend([path+'/'+f for f in dirnames])
        break
for a in dir: listAll(a)
print json.dumps(files, indent=4, sort_keys=True)
