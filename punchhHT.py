#! /usr/bin/env python

import os
import shutil
import json
from mod_pbxproj import *

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

home = os.path.expanduser("~")
input_json_path = home+"/Desktop/punchhHT_scriptTest/input.json"
if os.path.exists(input_json_path):
    input_json = json.load(open(input_json_path))
    for k in input_json:
        prPurple(k + " : " + input_json[k])
else:
    prRed("input.json not found at " + input_json_path)
    exit(1)

orignal_tmpt = home+"/.punchh/tmpt/PunchhPointBasedApp"
new_path = home+"/Desktop/punchhHT_scriptTest/"
if os.path.exists(new_path+"PunchhPointBasedApp/"):
     os.system("rm -rf " + new_path + "PunchhPointBasedApp/")
     prGreen("old dir removed.")
prGreen("copy...")
os.system("cp -r "+orignal_tmpt+" "+new_path)
prGreen("copy done.")

# sourceCode = XcodeProject.Load(new_path+"PunchhPointBasedApp/PunchhPointBasedApp.xcodeproj/project.pbxproj")
sourceCode = open(new_path+"PunchhPointBasedApp/PunchhPointBasedApp.xcodeproj/project.pbxproj").read()
# print sourceCode
projectName = input_json["projectName"]
sourceCode = sourceCode.replace("PunchhPointBasedApp", projectName)
rewritefile = open(new_path+"PunchhPointBasedApp/PunchhPointBasedApp.xcodeproj/project.pbxproj", "w")
rewritefile.write(sourceCode)
rewritefile.close()

#remove the xcuserdata file from the project
shutil.rmtree(new_path+"PunchhPointBasedApp/PunchhPointBasedApp.xcodeproj/xcuserdata")

os.rename(new_path+"PunchhPointBasedApp/PunchhPointBasedApp.xcodeproj", new_path+"PunchhPointBasedApp/"+projectName+".xcodeproj")
os.rename(new_path+"PunchhPointBasedApp/PunchhPointBasedApp", new_path+"PunchhPointBasedApp/"+projectName)


prRed("file content change")
