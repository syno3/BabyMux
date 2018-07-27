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

#banner before menu
banner.test()
time.sleep(3)

def main():
#displays number for different hacking tools
    print "BabyMux recommends the following tools:"
    time.sleep(1)
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
    print"13-batch-download\n"
    print"00-exit mars"

    babymux = raw_input("Select a tool to install>>")

# make a global do something
    def nmap():
        print subprocess.Popen("apt-get install -y nmap", shell=True, stdout=subprocess.PIPE).stdout.read()
        time.sleep(1)
        main()

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
