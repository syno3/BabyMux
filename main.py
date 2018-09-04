#!/usr/bin/env python

__author__ = "festus murimi"
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
#terminal colors

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

#banner before menu
banner.test()
time.sleep(3)

#Request for r007 access
if os.getuid() != 0:
	print("You need root access to run Babymux\n Use sudo")
	sys.exit(0)

def main():
#displays number for different hacking tools
    print "BabyMux recommends the following tools:"
    time.sleep(1)
    print"WARNING+1-metasploit - exploitation"
    print"WARNING+2-nmap - Discovery/OSINT/Vulnerability Analysis"
    print"WARNING+3-hulk - Stress teet"
    print"WARNING+4-Zmap - very fast scanner"
    print"WARNING+5-scapy"
    print"WARNING+6-subBrute-force"
    print"WARNING+7-sqlmap - SQLi/XSS Discovery/Exploitation"
    print"WARNING+8-xshell"
    print"WARNING+9-redhawk"
    print"WARNING+10-routersploit - exploitation"
    print"WARNING+11-hydra - password bruteforce"
    print"WARNING+12-breacher"
    print"WARNING+13-batch-download\n"
    print"WARNING+00-exit babyMux"

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
    elif babymux == '9' or babymux == '08':
        xshell()
    elif babymux == '10':
        red-hawk()
    elif babymux == '11':
        routersploit()
    elif babymux == '12':
        hydra()
    elif babymux == '13':
        breacher()
    elif babymux == '14':
        batch-download()
    elif babymux == '00':
        sys.exit()
    else:
        print "\n please enter a valid input"
        time.sleep(3)
        return main()

if __name__ == "__main__":
	main()
