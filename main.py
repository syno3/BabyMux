#!/usr/bin/env python

__author__ = "festus murimi and Tendel"
__title__ = "BabyMux"
__python_version__ = "v2.7.13"
__copyright__ = "copyright 2018, GPl v3.0"
#=================================

#importing modules needed

import time
import os
import sys
import subprocess
from core import banner
from core import core
import platform
#terminal colors
#please do not use terminal colors manualy, there is a python lib called termcolor 

#getting errors in displaying the banner, SyntaxError: Non-ASCII character '\xe2' on line 5 of banner.py 
#need root access to run the script
if os.getuid() != 0:
	print("You need root access to run Babymux\nUse sudo")
	sys.exit(0)
if ("debian" not in platform.platform() or "ubuntu" not in platform.platform()):
    print("This script was built to be run on debian like distros, you will need apt to run this script\nIf this is an false postive please report an issue to the github page")
    sys.exit(1)

def main():
#displays number for different tools
    print "BabyMux recommends the following tools:"
    print"1-metasploit - exploitation"
    print"2-nmap - Discovery/OSINT/Vulnerability Analysis"
    print"3-hulk - Stress teet"
    print"4-Zmap - very fast scanner"
    print"5-scapy"
    print"6-subBrute-force"
    print"7-sqlmap - SQLi/XSS Discovery/Exploitation"
    print"8-xshell"
    print"9-redhawk"
    print"10-routersploit - exploitation"
    print"11-hydra - password bruteforce"
    print"12-breacher"
    print"13-gobuster"
    print"14-batch-download all\n"
    print"00-exit babyMux"

    babymux = raw_input("Select a tool to install>>")
 
    if babymux =='1' or babymux == '01':
        metasploit()
    elif babymux == '2' or babymux == '02':
        nmap()
    elif babymux == '3' or babymux == '03':
        hulk()
    elif babymux == '4' or babymux == '04':
        Zmap()
    elif babymux == '5' or babymux == '05':
        scapy()
    elif babymux == '6' or babymux == '06':
        subBrute-force()
    elif babymux == '7' or babymux == '07':
        sqlmap()
    elif babymux == '8' or babymux == '08':
        xshell()
    elif babymux == '9':
        red-hawk()
    elif babymux == '10':
        routersploit()
    elif babymux == '11':
        hydra()
    elif babymux == '12':
        breacher()
    elif babymux == '13':
        gobuster()
    elif babymux == '14'
        batch-download()
    elif babymux == '00' or babymux == "0":
        sys.exit()
    else:
        print "\nPlease enter a valid input"
        main()
    return

if __name__ == "__main__":
    print "updating packages"
    os.system("apt update && apt upgrade")
    main()
