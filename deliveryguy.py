#!/usr/bin/env python
import sys

instructions_path="instructions.json"

# ---------------------------------------------------------------
process_error=False

class bcolors:
    HEADER = '\033[95m'
    OKCYAN = '\033[36m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printMsg(kMsgDesc,kQuit=False,kError=False):
    msg=getDate() + " - " + getHostname() + " - " + kMsgDesc
    if kError:
        print bcolors.FAIL + msg + bcolors.ENDC
    else:
        print bcolors.OKCYAN + msg + bcolors.ENDC

    if kQuit:
        import sys
        sys.exit(1)

def checkFileExistence(fileToCheck):
    import os
    return os.path.isfile(fileToCheck)

def getHostname():
    from socket import gethostname
    return str(gethostname())

def getDate():
    import datetime
    return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def loadJsonFile(filePath):
    import json
    try:
        data = json.loads(open(filePath).read())
        return data

    except:
        printMsg ("You're a bad boy! The JSON launch config is not correct. Go and check...",True,True)

def runScript(kScript):
    #todo
    try:
        print "runScript todo " + kScript

    except:
        printMsg ("runScript todo",True,True)

def copyFile(kSource,kDestination):
    global process_error
    import shutil
    try:
        shutil.copyfile(kSource,kDestination)

    except:
        process_error=True
        printMsg ("Error while copying " + kSource + " to " + kDestination,False,True)

def main(args):
    import datetime

    printMsg("Starting")

    printMsg("Working on " + instructions_path)

    if not checkFileExistence(instructions_path):
        printMsg("instructions_path not found",True,True)

    #Load JSON
    instructions=loadJsonFile(instructions_path)

    #Pull repo if any
    repo=instructions["repo"][0]
    if len(str(repo["url"])) > 0:
        printMsg("Found repo")
        printMsg("Cloning " + repo["url"] + "...")
        from subprocess import call
        call(["git", "clone", repo["url"], repo["destination"]])

    #Cycle instructions
    for task in instructions["instructions"]:

        #Check if a value has been specified
        if len(task["source"]) > 0 and len(task["destination"]) > 0:
            printMsg("Working on " + task["source"])

            #Check script before copy
            if len(task["run_before"]):
                runScript(task["run_before"])

            #Copy file
            copyFile(task["source"], task["destination"])

            #Check script after copy
            if len(task["run_after"]):
                runScript(task["run_after"])

    if process_error:
        printMsg("Process terminated with errors",False,True)
    else:
        printMsg("Process finished successfully")

if __name__ == "__main__":
    import os
    if len(sys.argv) > 1:
        instructions_path=str(sys.argv[1])
    else:
        instructions_path=os.path.dirname(os.path.abspath(__file__)) + "/" + instructions_path
    main(sys.argv)