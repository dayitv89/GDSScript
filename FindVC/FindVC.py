##########################################################################
###
### py27-terminal-cmd $ python FindVC.py <FOLEDER PATH>
###
### GauravDS Seo 08, 2016.
###
### Find the ViewController Names and super class name, rename VC name to 
### pretty name :: Purpose to make pretty name for Google Anlytics
###
##########################################################################

import sys
from os import walk
import os 
import platform
from pprint import pprint
import re
import json


if platform.system().lower() in ['linux', 'darwin']:
    INFO = "\033[1m\033[36m[*]\033[0m "
    WARN = "\033[1m\033[31m[!]\033[0m "
else:
    INFO = "[*] "
    WARN = "[!] "

class OCHeader(object):
	''' Represents an objective-c header file and it's methods, etc '''

	def __init__(self, file_path, lineNo, line, verbose=False):
		self.file_path = os.path.abspath(file_path)
		self.file_name = os.path.basename(self.file_path)
		self.lineNo = lineNo
		self.line = line
		self._class_name = None
		self._super_class_name = None
		self._pretty_class_name = None
		self._childs = []
		self.all_ok = False
		self.childOk = False
		self.superOk = False
		self.verbose = verbose
		# call all this
		if line:
			self.class_name()
			self.super_class_name()
			self.pretty_class_name()

	def printView(self): return str(self.class_name()) + " : " +str(self.super_class_name()) + " = " + str(self.pretty_class_name()) + " line " + self.line
	# def __str__(self): return self.printView()
	def __repr__(self): return self.printView()

	def toCSV(self): return str(self.class_name()) + "," +str(self.super_class_name()) + "," + str(self.pretty_class_name())

	def class_name(self):
		''' Get class name from source code '''
		if self._class_name is not None:
			return self._class_name
		else:
			if self.line.startswith('@interface'):
				class_name = self.line.split('@interface')[1].lstrip().split(' ')[0]
				if self.verbose: print(INFO + "Found class: %s" % class_name)
				self._class_name = class_name.strip()
				self.childOk = True
				return self._class_name

	def super_class_name(self):
		''' Get super class name from source code '''
		if self._super_class_name is not None:
			return self._super_class_name
		else:
			if self.line.startswith('@interface'):
				try: 
					super_class_name = self.line.split(':')[1]
					super_class_name = re.split('<|\n|\t|{| ', super_class_name.lstrip())[0]
					self._super_class_name = super_class_name.strip()
					if self._super_class_name not in self.superExcept:
						self.superOk = True
					if self.verbose: print(INFO + "Found superclass: %s" % super_class_name ) 
					return self._super_class_name
				except IndexError as error:
					pass

	def pretty_class_name(self):
		''' Get pretty name of class name '''
		if self._pretty_class_name is not None:
			return self._pretty_class_name
		else:
			if self.superOk and self.childOk:
				self.all_ok = True
				self._pretty_class_name = self.convertName(self.class_name())
				return self._pretty_class_name
			else:
				self._pretty_class_name = "class name not ok " + str(self._class_name)
			return self._pretty_class_name

	def addChilds(self, obj):
		if self._class_name == obj._super_class_name:
			self._childs.append(obj)
			return True
		else:
			for c in self._childs:
				if c.addChilds(obj):
					return True
			return False



### HELPER 
	keywordsReplace = { 
		"controller" : "Screen **",
		"Controller" : "Screen **",
		"view Screen **" : "Screen *",
		"View Screen **"  : "Screen *",
	}

	superExcept = ["NSObject", "UIView", "UILabel", "UIButton", "UITableViewCell", "UIImageView", "UITextField", "JSONModel"]

	def convertName(self, name):
		## camel to space sepecrate code 
		s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', name)
		s2 = re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)
		## convert words
		for key in self.keywordsReplace:
			s2 = s2.replace(key, self.keywordsReplace[key])
		return s2

#### MAIN LOGIC 
files = []
dirs = [sys.argv[1]]
ocfiles = []

linesExcept = ("//", "#")
lineInclude = ("@interface")

def listAll(path, ext):
	for (dirpath, dirnames, filenames) in walk(path):
		files.extend([path+'/'+f for f in filenames if f.endswith(ext)])
		dirs.extend([path+'/'+f for f in dirnames])
		break

### find valid OC line or not 
## @interface CLASSNAME : SUPERCLASS 
def regex(str):
	return bool(re.compile(r'(@interface)[^@]+:[^@]+').match(str))

def printDetails(filePath):
	lineNo = 0
	for line in open(filePath, 'r'):
		line = line.strip()
		if line.startswith(linesExcept): continue
		lineNo += 1
		if regex(line):
			oc = OCHeader(filePath, lineNo, line, verbose=False)
			if oc.all_ok: ocfiles.append(oc)

### finds all directories recursively into `dirs`; and finds only .h files into `files`
for a in dirs: listAll(a, ".h") 

# pprint(files)
for fl in files: printDetails(fl)

### Add some more root files
oc = OCHeader("not available", "not available", "@interface UIResponder : NSObject ")
ocfiles.append(oc)
oc = OCHeader("not available", "not available", "@interface UIViewController : UIResponder ")
ocfiles.append(oc)
oc = OCHeader("not available", "not available", "@interface GAITrackedViewController : UIViewController ")
ocfiles.append(oc)

# pprint(ocfiles)
def default(instance):
    return {k: v
            for k, v in vars(instance).items()
            if str(k).startswith('_')
            }

# print json.dumps(ocfiles, default=default)

## new exp
deleteNodes = []
for i in xrange(len(ocfiles)):
	oc1 = ocfiles[i]
	for j in xrange(len(ocfiles)):
		if i == j: pass
		if oc1.addChilds(ocfiles[j]):
			deleteNodes.append(j)

deleteNodes = list(set(deleteNodes))
for index in reversed(sorted(deleteNodes)):
	del ocfiles[index]

finalData = {}
for oc in ocfiles:
	if oc.super_class_name() not in finalData:
		finalData[oc.super_class_name()] = [oc]
	else:
		finalData[oc.super_class_name()].append(oc)


# use to convert CSV and xls :: https://json-csv.com/
print json.dumps(finalData, default=default)





