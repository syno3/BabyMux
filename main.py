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
from core import banner

def main():
#displays number for different hacking tools
    banner.test()
    time.sleep(3)
    print "select the values for the options of tools available\n"
    print"1-metaspoilt"
    print"2-nmap"
    print"3-hulk"
    print"4-Zmap"
    print"5-scapy"
    print"6-subBrute-force"
    print"7-sqlmap"
    print"8-xshell"
    print"9-redhawk"
    print"10-routerspoilt"
    print"11-hydra"
    print"12-breacher"
    print"13-batch-download\n"
    print"00-exit mars"

    babymux = raw_input("select your values>>")

    if babymux =='1' or babymux == '01':
        metaspoilt()
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
        routerspoilt()
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
        time.sleep(100)
        restart()

if __name__ == "__main__":
	main()
