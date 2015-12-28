#! /usr/bin/env python

import getopt, sys, os, shutil

home = os.path.expanduser("~")
orignal_tmpt = home+"/.punchh/tmpt/"
verbose = False

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

def readCMD():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hoc:n:p:v", ["help", "output=", "create=", "path=","name="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    createProjectCall = False
    global verbose
    # prCyan(opts)
    if len(opts) == 0 :
        usage()
    else:
        for o, a in opts:
            if o == "-v":
                verbose = True
                prCyan("verbose mode on")
            elif o in ("-h", "--help"):
                usage()
                # sys.exit()
            elif o in ("-c", "--create"):
                # output = a
                if a not in ("pointLinear", "pointRadial", "visit"):
                    prRed('spacify a valid type : -c ("pointLinear", "pointRadial", "visit")')
                    sys.exit()
                else:
                    createProjectCall = True
            # else:
            #     assert False, "type -h for help"
        if createProjectCall: createProject(opts, args)
def usage():
    info = """
-c --create : create new project; -c ("pointLinear", "pointRadial", "visit"); use as \n$punchhHT -c pointLinear\n
-n --name : project name; use as \n$punchhHT -c pointLinear -n "Point Based Linear" \n
-h --help : punchh hyper terminal help; use as $punchhHT -h\n
-p --path : project destination path; default is desktop; use as \n$punchhHT -c pointLinear -n "Point Based Linear" -p /user/username/Desktop/MyProjects/PunchhProjects/ \n
    """
    prPurple(info)

def createProject(opts, args):
    projectName = None
    projectType = None
    new_path = home + "/Desktop/"
    projectTypeEnum = {"pointLinear":"Punchh Point Based Linear", "pointRadial":"Punchh Point Based Radial", "visit":"Punchh Visit Based"}
    for o, a in opts:
        if o in ("-c", "--create"):
            projectType = projectTypeEnum[a]
        elif o in ("-n", "--name", "-pn", "--project-name"):
            projectName = a
        elif o in ("-p", "--path"):
            new_path = a
            if not new_path.endswith("/"): new_path += "/"
            if not os.path.exists(new_path): os.makedirs(new_path)

    projectNameSpc = projectType.replace(" ","\\ ")
    if os.path.exists(new_path+projectType):
        prRed("Project Destination path already exist: "+new_path+projectType)
        read = raw_input(" Want to replace (y/n): ")
        if read == 'y':
            rmCMD = "rm -rf " + new_path + projectNameSpc +"/"
            if verbose: prCyan(rmCMD)
            os.system(rmCMD)
        else:
            sys.exit()

    copyCMD = "cp -r "+orignal_tmpt+projectNameSpc+" "+new_path
    if verbose: prCyan("project is copying...")
    os.system(copyCMD)
    if projectName:
        sourceCode = open(new_path+projectType+"/"+projectType+".xcodeproj/project.pbxproj").read()
        sourceCode = sourceCode.replace(projectType, projectName)
        rewritefile = open(new_path+projectType+"/"+projectType+".xcodeproj/project.pbxproj", "w")
        rewritefile.write(sourceCode)
        rewritefile.close()

        shutil.rmtree(new_path+projectType+"/"+projectType+".xcodeproj/xcuserdata")
        os.rename(new_path+projectType+"/"+projectType+".xcodeproj", new_path+projectType+"/"+projectName+".xcodeproj")
        os.rename(new_path+projectType+"/"+projectType, new_path+projectType+"/"+projectName)
        os.rename(new_path+projectType,new_path+projectName)
    prGreen("DONE")
    prLightPurple("Project copied to: "+new_path)

readCMD()
