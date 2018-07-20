import time 
import os 
import sys


def metaspoilt():
    metaspoilt =  https://gist.githubusercontent.com/Gameye98/d31055c2d71f2fa5b1fe8c7e691b998c/raw/09e43daceac3027a1458ba43521d9c6c9795d2cb/msfinstall.sh
    print "====downloading metaspoilt"
	os.system("apt update && apt upgrade")
	os.system("apt install git wget curl")
	os.system("wget metaspoilt ")
	os.system("mv msfinstall.sh ~;cd ~;sh msfinstall.sh")
	print '###### Done'
	print "###### Type 'msfconsole' to start."
def nmap():
    print '=====downloading Nmap\n'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap')
	print '===== Done'
    print "===== Type 'nmap' to start."
def wireshark():
    pass
def zmap():
    pass
def scapy():
    pass
def subBrute-force():
    pass
def sqlmap():
    sqlmap = https://github.com/sqlmapproject/sqlmap
    print '===== downloading sqlmap'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/sqlmapproject/sqlmap')
	os.system('mv sqlmap ~')
	print '====Done'
def xshell():
    xshell = https://github.com/Ubaii/Xshell
    print '=====downloading Xshell'
	os.system("apt update && apt upgrade")
	os.system("apt install lynx python2 figlet ruby php nano w3m")
	os.system("git clone xshell")
	os.system("mv Xshell ~")
	print '======Done'
def red-hawk():
    red-hawk = https://github.com/Tuhinshubhra/RED_HAWK
    print '=====downloading RED HAWK\n'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone red-hawk')
	os.system('mv RED_HAWK ~')
	print '======Done'
def routerspoilt():
    routerspoilt = https://github.com/Tuhinshubhra/RED_HAWK
    print '====Installing Routersploit\n'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('pip2 install requests')
	os.system('git clone routersploit')
	os.system('mv routersploit ~;cd ~/routersploit;pip2 install -r requirements.txt;termux-fix-shebang rsf.py\n')
	print '=====Done'
def hydra():
    print "=====downloading hydra\n"
    os.system("apt upgarde && apt update")
    os.system("apt install hydra")
    print"======done\n"
def breacher():
    breacher = https://github.com/UltimateHackers/Breacher
    print '=====downloading Breacher\n'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('pip2 install requests argparse')
	os.system('git clone breacher')
	os.system('mv Breacher ~\n')
	print '=====Done'
def batch-download():
    permission = raw_input("this may lead  to high mobile traffic do you want to continue [Y/N]")
    if (permission == "Y" or permission == "y"):
        os.system("apt upgrade && apt update")
        try:
            pass
        except Exception as e:
            print"e"
    elif (permission == "N" or permission == "n"):
        pass
    else:
        print "please enter a valid input"
        
    
