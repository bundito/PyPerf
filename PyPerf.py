""" A small checker to keep performance apps running """

import os

from time import sleep
from win10toast import ToastNotifier

TOASTER = ToastNotifier()


def is_running(name):
    """ Checks Windows tastlist for process name """
    # call "tasklist", filtered to name of program
    # save to temp file for processing
    os.system('tasklist /FI "IMAGENAME eq %s" > tmp.txt' % name)

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

    return False

# End function is_running()

def check_loop():
    """ Loops through defined programs and checks if running """

    programs = (
        [
            "BorderlessGaming.exe",
            "Borderless Gaming",
            "C:\\Program Files (x86)\\Borderless Gaming\\BorderlessGaming.exe"
        ],
        [
            "ThrottleStop.exe",
            "ThrottleStop",
            "C:\\ThrottleStop_8.70.6\\ThrottleStop.exe"
        ],
        [
            "MSIAfterburner.exe",
            "MSI Afterburner",
            "C:\\Program Files (x86)\\MSI Afterburner\\MSIAfterburner.exe"
        ],
        )

    for prog in programs:
        proc_name = prog[0]
        pretty_name = prog[1]
        exe_name = prog[2]

        alive = is_running(proc_name)

        if not alive:
            TOASTER.show_toast("Performance Apps",
                               pretty_name + " went down. Restarting...",
                               icon_path="fast.ico")

            os.startfile(exe_name)

# END function checkloop

while True:
    check_loop()
    sleep(10)
