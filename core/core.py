# -*- coding: utf-8 -*-

import time
import os
import sys

"""global website variables"""
metaspoilt = 'https://github.com/rapid7/metasploit-framework'
hulk = 'https://github.com/grafov/hulk'
scapy = 'https://github.com/secdev/scapy'
subBrute_force = 'https://github.com/TheRook/subbrute'
sqlmap = 'https://github.com/sqlmapproject/sqlmap'
xshell = 'https://github.com/Ubaii/Xshell'
red_hawk = 'https://github.com/Tuhinshubhra/RED_HAWK'
routerspoilt = 'https://github.com/reverse-shell/routersploit'
breacher = 'https://github.com/UltimateHackers/Breacher'
def metaspoilt():
	print "====downloading metaspoilt\n"
	os.system("apt install git wget curl")
	os.system("wget metaspoilt ")
	os.system("mv msfinstall.sh ~;cd ~;sh msfinstall.sh")
	print '=====Done'
	print "===== Type 'msfconsole' to start."
def nmap():
	print '=====downloading Nmap\n'
	os.system('apt install nmap')
	print '===== Done'
	print "===== Type 'nmap' to start."
def hulk():
	print"====downlaoding hulk\n"
	os.system("git clone "+hulk)
	os.system("mv Hulk ~\n")
	permission = raw_input("do you want to test hulk [Y/N]")
	if (permission == "Y" or permission == "y"):
		website = raw_input("please enter the vulnerable website")
		os.system("cd ~;cd hulk;python hulk.py website")
	else:
		print "===download done\n"
		sys.exit()
def zmap():
	print "====downloading zmap\n"
	os.sytem("apt install zmap")
	print"====downloading done"
def scapy():
	print"====downloading scapy\n"
	os.system("git clone " + scapy)
	permission = raw_input("do you want to run scapy [Y/N]")
	if (permission == "Y" or permission == "y"):
		os.system("cd scapy")
		os.system("./run_scapy")
	else:
		print "====download done"
		sys.exit()
def subBrute_force():
	print("====downloading subBrute-force")
	os.system("git clone " + subBrute_force)
	permission = raw_input("do you want to test subbrute-force [Y/N]")
	if (permission == "Y" or permission ==  "y"):
		print"===downloading python-dnspython"
		os.sytem("sudo apt-get install python-dnspython")
		website = raw_input("what website would you like to test\n")
		os.system("./subbrute.py website")
	else:
		print "===download done"
		sys.exit()
def sqlmap():
	print ('===== downloading sqlmap')
	# os.system('apt install git python2')
	os.system('git clone sqlmap')
	os.system('mv sqlmap ~')
	print '====Done'
def xshell():
	print '=====downloading Xshell\n'	
	os.system("apt install lynx python2 figlet ruby php nano w3m")
	os.system("git clone xshell")
	os.system("mv Xshell ~")
	print '======Done'
def red_hawk():
	print '=====downloading RED HAWK\n'
	os.system('apt install git php')
	os.system('git clone ' + red_hawk)
	os.system('mv RED_HAWK ~')
	print '======Done'
def routerspoilt():
	print '====Installing Routersploit\n'
	os.system('apt install python2 git')
	os.system('pip2 install requests')
	os.system('git clone' + routersploit)
	os.system('mv routersploit ~;cd ~/routersploit;pip2 install -r requirements.txt;termux-fix-shebang rsf.py\n')
	print '=====Done'
def hydra():
	print "=====downloading hydra\n"
	os.system("apt install hydra")
	print"======done\n"
def breacher():
	print '=====downloading Breacher\n'
	os.system('apt install git python2')
	os.system('pip2 install requests argparse')
	os.system('git clone' + breacher)
	os.system('mv Breacher ~\n')
	print '=====Done'
def gobuster():
        print '=====downloading GoBuster and installing Go'
        os.system("apt install go")
        os.system("go get github.com/OJ/gobuster")
def batch_download():
	permission = raw_input("this may lead  to high mobile traffic do you want to continue [Y/N]")
	if (permission == "Y" or permission == "y"):
            try:
                metasploit()
                nmap()
                hulk()
                zmap()
                scapy()
                subBrute_force()
                sqlmap()
                xshell()
                red_hawk()
                routerspoilt()
                hydra()
                breacher()
                gobuster()
            except Exception:
			traceback.print_exc(file=sys.stdout)
			print "Some Packages have not been downloaded\n Please check your Internet connection"
			return 
        else:
            print "Not running batch script"
            sys.exit(1)
