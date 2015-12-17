import requests
from pwn import *


import sys
import socket
import string
from subprocess import call

from Crypto.Cipher import AES
from Crypto.Hash import SHA256





stopFlag = False
while not stopFlag:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	args = 'a' * 1024
	s.connect(("csie.ctf.tw", 10122))
	Nc = '945'
	s.send('fox||' + Nc + '\n')

	data = s.recv(4096)
		# print 'no'
	if not data:
		exit(0)

		
	data_string = str(data)
		
	print(data_string)



	Ns = data_string.split('||')[1]

	if Ns == '213':
		stopFlag = True
		print 'going to stop'
	# message = 'key||' + Nc + '||' + Ns
	# sha256 = SHA256.new()
	# sha256.update(message)
	# s.send( base64.b64encode(sha256.digest()) + '\n')

	# s.send('fox||' + Ns + '\n')
	tt = '\x59\x4d\x6b\x4b\x4e\x39\x72\x62\x6b\x69\x50\x56\x63\x74\x59\x4f\x6f\x32\x4b\x5a\x78\x73\x5a\x53\x6c\x30\x48\x63\x66\x72\x50\x6d\x79\x59\x78\x2f\x6c\x52\x74\x76\x71\x35\x63\x3d\x0a'
	print tt

	s.send(tt + '\n')
	data = s.recv(4096)
		# print 'no'
	if not data:
		exit(0)

		
	data_string = str(data)
		
	print(data_string)

	data = s.recv(4096)
		# print 'no'
	if not data:
		exit(0)

		
	data_string = str(data)
		
	print(data_string)
	s.close()





	
		
		





