##########################################################################
###
### terminal$ python CCArc.py
###
### GauravDS Apr 22, 2015.
###
### Add ARC disable flag '-fno-objc-arc' to cocos2d files starting with CC
###
##########################################################################

import os

xcodeFile = [f for f in os.listdir('.') if f.endswith('.xcodeproj')]

if len(xcodeFile) == 0:
    print "Could not find .xcodeproj File, place this python file where your .xcodeproj file"
    exit()

f = open(xcodeFile[0]+'/project.pbxproj')

Alllines = ''

fileAdded = 0

for line in f.readlines():
    if line.find('/* CC') != -1 and line.find('in Sources */') != -1:
        if line.find('settings = {COMPILER_FLAGS = "-fno-objc-arc"; };') == -1 and line.endswith('};\n'):
            print line
            line = line[:-3] + ' settings = {COMPILER_FLAGS = "-fno-objc-arc"; }; ' + line[-3:]
            print "compiler flag added"
            print line
            print '------------'
            fileAdded = fileAdded + 1
#        else:
#            print line
#            print '@@@@@@@@@@@@@@'

    Alllines = Alllines + line

f.close()

if fileAdded != 0:
    print '\n\nFlag added to ' + str(fileAdded) + ' file(s).\n\n'
    fw = open(xcodeFile[0]+'/project.pbxproj','w');
    fw.write( str(Alllines)  )
    fw.close()
    print "Step 1: Close the xcode\nStep 2: copy 'project.pbxproj'\nStep 3: Right click on .xcodeproj file\nStep 4: Tap on 'Show package contents'\nStep 5: Paste 'project.pbxproj', asking for replace then tap replace. \nStep 6: Reopen the XCode project and Voila!\n\n"
else:
    print "No need to updated any thing"

