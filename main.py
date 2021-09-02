#!/usr/bin/env python

__author__ = "festus murimi"
__title__ = "BabyMux"
__python_version__ = "v3.3"
__copyright__ = "copyright 2020, GPl v3.0"
#=================================

#importing modules needed
try :
	import time
	import os
	import sys
	from banner import test
	import logging
except Exception as e:
	logging.error(e)


#### GLOBAL VARIABLES FOR COLORS

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

### BABYMUX CLASS
class Babymux:
	def __init__(self):
		self.metaspoilt = 'https://github.com/rapid7/metasploit-framework.git'
		self.hulk = 'https://github.com/grafov/hulk.git'
		self.scapy = 'https://github.com/secdev/scapy.git'
		self.subBrute_force = 'https://github.com/TheRook/subbrute.git'
		self.sqlmap = 'https://github.com/sqlmapproject/sqlmap.git'
		self.xshell = 'https://github.com/Ubaii/Xshell.git'
		self.red_hawk = 'https://github.com/Tuhinshubhra/RED_HAWK.git'
		self.routerSpoilt = 'https://github.com/threat9/routersploit.git'
		self.breacher = 'https://github.com/s0md3v/Breacher.git'

	def metaspoilt(self):
		print ("====downloading metaspoilt\n")
		os.system("python -m pip install --upgrade")
		os.system("python -m pip install git wget curl")
		os.system("wget metaspoilt ")
		os.system("mv msfinstall.sh ~;cd ~;sh msfinstall.sh")
		print ('=====Done')
		print ("===== Type 'msfconsole' to start.")

	def nmap(self):
		print ('=====downloading Nmap\n')
		os.system('python -m pip install --upgrade')
		os.system('python -m pip install nmap')
		print ('===== Done')
		print ("===== Type 'nmap' to start.")

	def hulk(self):
		print ("====downlaoding hulk\n")
		os.system("git clone {}").format(self.hulk)
		os.system("mv Hulk ~\n")
		permission = input("do you want to test hulk [Y/N]: ")
		if (permission == "Y" or permission == "y"):
			website = input("please enter the vulnerable website: ")
			os.system("cd ~;cd hulk;python hulk.py" + website)
		else:
			print ("===download done\n")
			time.sleep(3)
			sys.exit()

	def zmap(self):
		print ("====downloading zmap\n")
		os.system("apt upgarde && apt update")
		os.system("sudo python -m pip install zmap")
		print ("====downloading done")

	def scapy(self):
		print ("====downloading scapy\n")
		os.system("apt upgarde && apt update")
		os.system("git clone {}").format(self.scapy)
		permission = input("do you want to run scapy [Y/N]")
		if (permission == "Y" or permission == "y"):
			os.system("cd scapy")
			os.system("./run_scapy")
		else:
			print ("====download done")
			time.sleep(3)
			sys.exit()

	def subBrute_force(self):
		print("====downloading subBrute-force")
		os.system("apt upgrade && apt upgrade")
		os.system("git clone ").format(self.subBrute_force)
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

	def sqlmap(self):
		print ('===== downloading sqlmap')
		os.system('python -m pip install --upgrade')
		# os.system('python -m pip install git python')
		os.system('git clone sqlmap')
		os.system('mv sqlmap ~')
		print ('====Done')

	def xshell(self):
		print ('=====downloading Xshell\n')
		os.system("python -m pip install --upgrade")
		os.system("python -m pip install lynx python figlet ruby php nano w3m")
		os.system("git clone xshell")
		os.system("mv Xshell ~")
		print ('======Done')

	def red_hawk(self):
		print ('=====downloading RED HAWK\n')
		os.system('python -m pip install --upgrade')
		os.system('python -m pip install git php')
		os.system('git clone {}').format(self.red_hawk)
		os.system('mv RED_HAWK ~')
		print ('======Done')

	def routerspoilt(self):
		print ('====Installing Routersploit\n')
		os.system('python -m pip install --upgrade')
		os.system('python -m pip install python git')
		os.system('pip2 install requests')
		os.system('git clone https://github.com/reverse-shell/routersploit')
		os.system('mv routersploit ~;cd ~/routersploit;pip2 install -r requirements.txt;termux-fix-shebang rsf.py\n')
		print ('=====Done')

	def hydra(self):
		print ("=====downloading hydra\n")
		os.system("apt upgarde && apt update")
		os.system("python -m pip install hydra")
		print ("======done\n")

	def breacher(self):
		print ('=====downloading Breacher\n')
		os.system('python -m pip install --upgrade')
		os.system('python -m pip install git python')
		os.system('pip2 install requests argparse')
		os.system('git clone {}').format(self.breacher)
		os.system('mv Breacher ~\n')
		print ('=====Done')

	def batch_download(self):
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
				os.system("git clone {}").format(self.hulk)
				os.system("mv Hulk ~\n")
				print ("===download done\n\n")
				time.sleep(3)
				print("====downloading zmap\n")
				os.system("apt upgarde && apt update")
				os.system("sudo python -m pip install zmap")
				time.sleep(3)
				print ("====downloading scapy\n")
				os.system("apt upgarde && apt update")
				os.system("git clone {}").format(self.scapy)
				time.sleep(3)
				print ("====downloading subBrute-force\n")
				os.system("apt upgrade && apt upgrade")
				os.system("git clone {}").format(self.subBrute_force)
				time.sleep(3)
				print ('===== downloading sqlmap\n')
				os.system('python -m pip install --upgrade')
				os.system('python -m pip install git python')
				os.system('git clone {}').format(self.sqlmap)
				time.sleep(3)
				print ('=====downloading Xshell\n')
				os.system("python -m pip install --upgrade")
				os.system("python -m pip install lynx python figlet ruby php nano w3m")
				os.system("git clone {}").format(self.xshell)
				os.system("mv Xshell ~")
				print ('======Done')
				time.sleep(3)
				print ('=====downloading RED HAWK\n')
				os.system('python -m pip install --upgrade')
				os.system('python -m pip install git php')
				os.system('git clone {}').format(self.red_hawk)
				os.system('mv RED_HAWK ~')
				print ('======Done')
				time.sleep(3)
				print ('====Installing Routersploit\n')
				os.system('python -m pip install --upgrade')
				os.system('python -m pip install python git')
				os.system('pip2 install requests')
				os.system('git clone {}').format(self.routerSpoilt)
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
				os.system('git clone {}').format(self.breacher)
				os.system('mv Breacher ~\n')
				print ("=== batch download done\n\n")

			except Exception:
				print("Some Packages have not been downloaded\n Please check your Internet connection")
				time.sleep(3)
				return self.batch_download

	def run(self):
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
			self.metaspoilt()
		elif babymux == '2' or babymux == '02':
			self.nmap()
		elif babymux == '3' or babymux == '03':
			self.hulk()
		elif babymux == '4' or babymux == '04':
			self.zmap()
		elif babymux == '5' or babymux == '05':
			self.scapy()
		elif babymux == '6' or babymux == '06':
			self.subBrute_force()
		elif babymux == '7' or babymux == '07':
			self.sqlmap()
		elif babymux == '9' or babymux == '08':
			self.xshell()
		elif babymux == '10':
			self.red_hawk()
		elif babymux == '11':
			self.routerspoilt()
		elif babymux == '12':
			self.hydra()
		elif babymux == '13':
			self.breacher()
		elif babymux == '14':
			self.batch_download()
		elif babymux == '00':
			sys.exit()
		else:
			print ("\n please enter a valid input")
			time.sleep(3)






Babymux = Babymux()
Babymux.run()
