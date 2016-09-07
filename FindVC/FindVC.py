import sys
from os import walk
import os 
import platform
from pprint import pprint
import re


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
		self.all_ok = False
		self.verbose = verbose
		# call all this
		self.class_name()
		self.super_class_name()
		self.pretty_class_name()

	def printView(self): return str(self.class_name()) + " : " +str(self.super_class_name()) + " = " + str(self.pretty_class_name()) + " line " + self.line
	def __str__(self): return self.printView()
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
				self.all_ok = True
				return self._class_name

	def super_class_name(self):
		''' Get super class name from source code '''
		if self._super_class_name is not None:
			return self._super_class_name
		else:
			if self.line.startswith('@interface'):
				try: 
					super_class_name = self.line.split(':')[1]
					super_class_name = re.split('<|\n|\t| ', super_class_name.lstrip())[0]
					if self.verbose: print(INFO + "Found superclass: %s" % super_class_name)
					self._super_class_name = super_class_name.strip()
					if self._super_class_name not in self.superExcept:
						self.all_ok = True
					else:
						self.all_ok = False
					return self._super_class_name
				except IndexError as error:
					pass

	def pretty_class_name(self):
		''' Get pretty name of class name '''
		if self._pretty_class_name is not None:
			return self._pretty_class_name
		else:
			## main logic
			if self.all_ok:
				self._pretty_class_name = self.convertName(self.class_name())
				return self._pretty_class_name
			else:
				self._pretty_class_name = "class name not ok " + str(self._class_name)
			return self._pretty_class_name


### HELPER 
	keywordsReplace = { 
		"View Controller" : "Screen",
		"view Controller" : "Screen",
		"view controller" : "Screen",
		"View" : "VIEW***",
		"view" : "VIEW***"
	}

	superExcept = ["NSObject", "UIView", "UIViewController", "UITabBarController", "SFSafariViewController", "JSONModel"]

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
			oc = OCHeader(filePath, lineNo, line)
			if oc.all_ok: ocfiles.append(oc)

### finds all directories recursively into `dirs`; and finds only .h files into `files`
for a in dirs: listAll(a, ".h") 

# pprint(files)
for fl in files: printDetails(fl)

# pprint(ocfiles)

print json.dumps(ocfiles)





