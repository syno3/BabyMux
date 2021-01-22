#!/usr/bin/env python

__author__ = "festus murimi"
__title__ = "BabyMux"
__python_version__ = "v3.3"
__copyright__ = "copyright 2020, GPl v3.0"
#=================================

#importing modules needed

import time
import os
import sys
from banner import test
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
os.system("cls")
test()
time.sleep(3)

#variables
"""global website variables"""
metaspoilt__ = 'https://github.com/rapid7/metasploit-framework'
hulk__ = 'https://github.com/grafov/hulk'
scapy__ = 'https://github.com/secdev/scapy'
subBrute_force__ = 'https://github.com/TheRook/subbrute'
sqlmap__ = 'https://github.com/sqlmapproject/sqlmap'
xshell__ = 'https://github.com/Ubaii/Xshell'
red_hawk__ = 'https://github.com/Tuhinshubhra/RED_HAWK'
routerSpoilt__ = 'https://github.com/reverse-shell/routersploit'
breacher__ = 'https://github.com/UltimateHackers/Breacher'


def main():
#displays number for different hacking tools
    print ("BabyMux recommends the following tools:\n\n")
    time.sleep(1)
    print(WARNING+"1-metasploit - exploitation")
    print(WARNING+"2-nmap - Discovery/OSINT/Vulnerability Analysis")
    print(WARNING+"3-hulk - Stress teet")
    print(WARNING+"4-Zmap - very fast scanner")
    print(WARNING+"5-scapy")
    print(WARNING+"6-subBrute-force")
    print(WARNING+"7-sqlmap - SQLi/XSS Discovery/Exploitation")
    print(WARNING+"8-xshell")
    print(WARNING+"9-redhawk")
    print(WARNING+"10-routersploit - exploitation")
    print(WARNING+"11-hydra - password bruteforce")
    print(WARNING+"12-breacher")
    print(WARNING+"13-batch-download\n")
    print(WARNING+"00-exit babyMux")

    babymux = input("Select a tool to install>> ")

    if babymux =='1' or babymux == '01':
        metaspoilt()
    elif babymux == '2' or babymux == '02':
        nmap()
    elif babymux == '3' or babymux == '03':
        hulk()
    elif babymux == '4' or babymux == '04':
        zmap()
    elif babymux == '5' or babymux == '05':
        scapy()
    elif babymux == '6' or babymux == '06':
        subBrute_force()
    elif babymux == '7' or babymux == '07':
        sqlmap()
    elif babymux == '9' or babymux == '08':
        xshell()
    elif babymux == '10':
        red_hawk()
    elif babymux == '11':
        routerspoilt()
    elif babymux == '12':
        hydra()
    elif babymux == '13':
        breacher()
    elif babymux == '14':
        batch_download()
    elif babymux == '00':
        sys.exit()
    else:
        print ("\n please enter a valid input")
        time.sleep(3)

#functions
def metaspoilt():
    print ("====downloading metaspoilt\n")
    os.system("python -m pip install --upgrade")
    os.system("python -m pip install git wget curl")
    os.system("wget metaspoilt ")
    os.system("mv msfinstall.sh ~;cd ~;sh msfinstall.sh")
    print ('=====Done')
    print ("===== Type 'msfconsole' to start.")

def nmap():
	print ('=====downloading Nmap\n')
	os.system('python -m pip install --upgrade')
	os.system('python -m pip install nmap')
	print ('===== Done')
	print ("===== Type 'nmap' to start.")

def hulk():
	print ("====downlaoding hulk\n")
	os.system("git clone "+hulk__)
	os.system("mv Hulk ~\n")
	permission = input("do you want to test hulk [Y/N]: ")
	if (permission == "Y" or permission == "y"):
		website = input("please enter the vulnerable website: ")
		os.system("cd ~;cd hulk;python hulk.py" + website)
	else:
		print ("===download done\n")
		time.sleep(3)
		sys.exit()

def zmap():
	print ("====downloading zmap\n")
	os.system("apt upgarde && apt update")
	os.system("sudo python -m pip install zmap")
	print ("====downloading done")

def scapy():
	print ("====downloading scapy\n")
	os.system("apt upgarde && apt update")
	os.system("git clone " + scapy__)
	permission = input("do you want to run scapy [Y/N]")
	if (permission == "Y" or permission == "y"):
		os.system("cd scapy")
		os.system("./run_scapy")
	else:
		print ("====download done")
		time.sleep(3)
		sys.exit()

def subBrute_force():
	print("====downloading subBrute-force")
	os.system("apt upgrade && apt upgrade")
	os.system("git clone " + subBrute_force__)
	permission = input("do you want to test subbrute-force [Y/N]")
	if (permission == "Y" or permission ==  "y"):
		print ("===downloading python-dnspython")
		time.sleep(2)
		os.system("sudo pip install python-dns python")
		os.system("./subbrute.py website")
	else:
		print ("===download done")
		time.sleep(3)
		sys.exit()

def sqlmap():
	print ('===== downloading sqlmap')
	os.system('python -m pip install --upgrade')
	# os.system('python -m pip install git python')
	os.system('git clone sqlmap')
	os.system('mv sqlmap ~')
	print ('====Done')

def xshell():
	print ('=====downloading Xshell\n')
	os.system("python -m pip install --upgrade")
	os.system("python -m pip install lynx python figlet ruby php nano w3m")
	os.system("git clone xshell")
	os.system("mv Xshell ~")
	print ('======Done')

def red_hawk():
	print ('=====downloading RED HAWK\n')
	os.system('python -m pip install --upgrade')
	os.system('python -m pip install git php')
	os.system('git clone ' + red_hawk__)
	os.system('mv RED_HAWK ~')
	print ('======Done')

def routerspoilt():
	print ('====Installing Routersploit\n')
	os.system('python -m pip install --upgrade')
	os.system('python -m pip install python git')
	os.system('pip2 install requests')
	os.system('git clone https://github.com/reverse-shell/routersploit')
	os.system('mv routersploit ~;cd ~/routersploit;pip2 install -r requirements.txt;termux-fix-shebang rsf.py\n')
	print ('=====Done')

def hydra():
	print ("=====downloading hydra\n")
	os.system("apt upgarde && apt update")
	os.system("python -m pip install hydra")
	print ("======done\n")

def breacher():
	print ('=====downloading Breacher\n')
	os.system('python -m pip install --upgrade')
	os.system('python -m pip install git python')
	os.system('pip2 install requests argparse')
	os.system('git clone' + breacher__)
	os.system('mv Breacher ~\n')
	print ('=====Done')

def batch_download():
	permission = input("this may lead  to high mobile traffic do you want to continue [Y/N]")
	if (permission == "Y" or permission == "y"):
		os.system("apt upgrade && apt update")
		try:
			print ("===downloading metaspoilt\n")
			os.system("python -m pip install --upgrade")
			os.system("python -m pip install git wget curl")
			os.system("wget metaspoilt ")
			time.sleep(3)
			print ('=====downloading Nmap\n')
			os.system('python -m pip install --upgrade')
			os.system('python -m pip install nmap')
			print ('===== Done\n\n')
			time.sleep(3)
			print ("====downlaoding hulk\n")
			os.system("git clone" + hulk)
			os.system("mv Hulk ~\n")
			print ("===download done\n\n")
			time.sleep(3)
			print("====downloading zmap\n")
			os.system("apt upgarde && apt update")
			os.system("sudo python -m pip install zmap")
			time.sleep(3)
			print ("====downloading scapy\n")
			os.system("apt upgarde && apt update")
			os.system("git clone "+scapy__)
			time.sleep(3)
			print ("====downloading subBrute-force\n")
			os.system("apt upgrade && apt upgrade")
			os.system("git clone " + subBrute_force__)
			time.sleep(3)
			print ('===== downloading sqlmap\n')
			os.system('python -m pip install --upgrade')
			os.system('python -m pip install git python')
			os.system('git clone ' + sqlmap__)
			time.sleep(3)
			print ('=====downloading Xshell\n')
			os.system("python -m pip install --upgrade")
			os.system("python -m pip install lynx python figlet ruby php nano w3m")
			os.system("git clone " + xshell__)
			os.system("mv Xshell ~")
			print ('======Done')
			time.sleep(3)
			print ('=====downloading RED HAWK\n')
			os.system('python -m pip install --upgrade')
			os.system('python -m pip install git php')
			os.system('git clone ' + red_hawk__)
			os.system('mv RED_HAWK ~')
			print ('======Done')
			time.sleep(3)
			print ('====Installing Routersploit\n')
			os.system('python -m pip install --upgrade')
			os.system('python -m pip install python git')
			os.system('pip2 install requests')
			os.system('git clone https://github.com/reverse-shell/routersploit')
			os.system('mv routersploit ~;cd ~/routersploit;pip2 install -r requirements.txt;termux-fix-shebang rsf.py\n')
			print ("===download done\n\n")
			time.sleep(3)
			print ("=====downloading hydra\n")
			os.system("apt upgarde && apt update")
			os.system("python -m pip install hydra")
			print ("======done\n")
			time.sleep(3)
			print ('=====downloading Breacher\n')
			os.system('python -m pip install --upgrade')
			os.system('python -m pip install git python')
			os.system('pip2 install requests argparse')
			os.system('git clone ' + breacher__)
			os.system('mv Breacher ~\n')
			print ("=== batch download done\n\n")
		except Exception:
			print("Some Packages have not been downloaded\n Please check your Internet connection")
			time.sleep(3)
			return batch_download()

if __name__ == "__main__":
	main()
