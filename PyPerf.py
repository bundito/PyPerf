
import os
def isRunning(name):

    # call "tasklist", filtered to name of program
    # save to temp file for processing
    os.system('tasklist /FI "IMAGENAME eq %s" /FI "STATUS eq running" > tmp.txt' % name)
    
    # read back the output of tasklist
    tmp = open('tmp.txt', 'r')
    file = tmp.readlines()
    tmp.close()

    # last line of output should be a successful output from tasklist - like this
    #   Image Name                     PID Session Name        Session#    Mem Usage
    #   ========================= ======== ================ =========== ============
    #   BorderlessGaming.exe         10852 Console                    2     14,936 K
    #
    # So we want the last line (file[-1]), split by spaces and the first entry - split()[0]
    if file[-1].split()[0] == name:
        return True
    else:
        return False

# End function isRunning()

programs = (
    ["BorderlessGaming.exe", "Borderless Gaming", "C:\Program Files (x86)\Borderless Gaming\BorderlessGaming.exe"],
    ["ThrottleStop.exe", "ThrottleStop", "C:\ThrottleStop_8.70.6\ThrottleStop.exe"],
    ["MSIAfterburner.exe", "MSI Afterburner", "C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe"]
    )

for prog in programs:
    procName = prog[0]
    prettyName = prog[1]
    exeName = prog[2]

    alive = isRunning(procName)

    if alive:
        print("%s is running", prettyName)
    else:
        print("It appears %s is down.", prettyName)


    
