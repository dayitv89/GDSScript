import getopt, sys, os

home = os.path.expanduser("~")
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
    if len(opts) == 0 :
        usage()
    else:
        for o, a in opts:
            if o == "-v":
                verbose = True
                prRed("verbose mode on")
            elif o in ("-h", "--help"):
                usage()
                # sys.exit()
            elif o in ("-c", "--create"):
                # output = a
                if a not in ("pointLinear", "pointRadial", "visit"):
                    prRed('spacify a valid type : -c ("pointLinear", "pointRadial", "visit")')
                    sys.exit()
                else:
                    createProject(opts, args)
            else:
                assert False, "type -h for help"
def usage():
    info = """
-c --create : create new project; use as \n$punchhHT -c pointLinear\n
-n --name : project name; use as \n$punchhHT -c pointLinear -n "Point Based Linear" \n
-h --help : punchh hyper terminal help; use as $punchhHT -h\n
-p --path : project destination path; default is desktop; use as \n$punchhHT -c pointLinear -n "Point Based Linear" -p /user/username/Desktop/MyProjects/PunchhProjects/ \n
    """
    prPurple(info)

def createProject(opts, args):
    projectName = None
    projectType = None
    projectPath = home + "/Desktop/"
    projectTypeEnum = {"pointLinear":0, "pointRadial":1, "visit":2}
    for o, a in opts:
        if o in ("-c", "--create"):
            projectType = projectTypeEnum[a]
        elif o in ("-n", "--name", "-pn", "--project-name"):
            projectName = a
        elif o in ("-p", "--path"):
            projectPath = a
    prLightPurple(projectName)
    prLightPurple(projectType)
    prLightPurple(projectPath)

readCMD()
