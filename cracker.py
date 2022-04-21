import os
import sys
import time

def mengetik(s):
	for c in s + '\n' :
        	sys.stdout.write(c)
        	sys.stdout.flush()
        	time.sleep(3 /50)

def mulai():
	os.system("clear")
	mengetik("\033[32;1mMohon Maaf Script Sedang Maintenance !\n")
	time.sleep(1)
	mengetik("\033[32;1mSilahkan Tunggu Besok !")
	time.sleep(2)
	os.system("exit")

#mulai
os.system("git pull")
mulai()
