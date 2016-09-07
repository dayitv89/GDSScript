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

def printDetails(filePath):
	val = ''
	lineNo = 0
	for line in open(filePath, 'r'):
		line = line.strip()
		if line.startswith(linesExcept): continue
		lineNo += 1
		if line.startswith("@interface"):
			oc = OCHeader(filePath, lineNo, line)
			if oc.all_ok:	ocfiles.append(oc)
			val += 'Line: '+str(lineNo)+' => '+line+'\n'
	# print val

class OCHeader(object):
	''' Represents an objective-c header file and it's methods, etc '''

	def __init__(self, file_path, lineNo, line, verbose=False):
		self.file_path = os.path.abspath(file_path)
		self.file_name = os.path.basename(self.file_path)
		self.lineNo = lineNo
		self.line = line
		self._class_name = None
		self._super_class_name = None
		self.all_ok = True
		self._pretty_class_name = None
		self.verbose = verbose
		self.class_name()
		self.super_class_name()
		self.pretty_class_name()

	def __str__(self):
		return str(self.class_name()) + " : " +str(self.super_class_name()) + " = " + str(self.pretty_class_name())

	def __repr__(self):
		return str(self.class_name()) + " : " +str(self.super_class_name()) + " = " + str(self.pretty_class_name())

	def class_name(self):
		''' Get class name from source code '''
		if self._class_name is not None:
			return self._class_name
		else:
			if self.line.startswith('@interface'):
				class_name = self.line.split(' ')[1]
				if self.verbose: print(INFO + "Found class: %s" % class_name)
				self._class_name = class_name.strip()
				self._all_ok = True
				return self._class_name

	def super_class_name(self):
		''' Get super class name from source code '''
		if self._super_class_name is not None:
			return self._super_class_name
		else:
			if self.line.startswith('@interface'):
				try: 
					super_class_name = self.line.split(':')[1]
					super_class_name = re.split('<|\n| ', super_class_name.lstrip())[0]
					if self.verbose: print(INFO + "Found superclass: %s" % super_class_name)
					self._super_class_name = super_class_name.strip()
					self._all_ok = True
					return self._super_class_name
				except IndexError as error:
					pass

	def pretty_class_name(self):
		''' Get pretty name of class name '''
		if self._pretty_class_name is not None:
			return self._pretty_class_name
		else:
			## main logic
			# temp logic
			if self.all_ok:
				self._pretty_class_name = self.class_name()
				return self._pretty_class_name
			return "class name not found"
	


### finds all directories recursively into `dirs`; and finds only .h files into `files`
for a in dirs: listAll(a, ".h") 

# pprint(files)
for fl in files: printDetails(fl)

pprint(ocfiles)






