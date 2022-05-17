import os
import sys
import time

def mengetik(s):
	for c in s + '\n' :
        	sys.stdout.write(c)
        	sys.stdout.flush()
        	time.sleep(3 /100)

def mulai():
	os.system("clear")
	mengetik("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] \x1b[1;92mMohon Maaf Script Sedang Maintenance !\n")
	time.sleep(1)
	mengetik("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] \x1b[1;92mSilahkan Coba Jalankan Ulang Script Secara Berkala Agar Tidak Ketinggalan Update!")
	time.sleep(2)
	os.system("exit")

#mulai
os.system("git pull")
mulai()
