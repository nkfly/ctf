import requests

import hashlib

import sys
import socket
import string
from subprocess import call

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# args = 'a' * 1024 nc 52.69.244.164 9003
s.connect(("52.69.244.164", 9003))

def make_answer(begin_0, begin_1, begin_2, begin_3):
	
	
	answer = chr(int(begin_0, 16)) + chr(int(begin_1, 16)) + chr(int(begin_2, 16)) + chr(int(begin_3, 16))


	for i in range(256):
		for j in range(256):
			for k in range(256):
				for m in range(256):
					hashing = hashlib.sha1()
					tmp_answer = answer + chr(i) + chr(j) + chr(k) + chr(m)

					hashing.update(tmp_answer)
					if hashing.digest()[0:3] == '\x00\x00\x00':
						print hashing.hexdigest()
						print hashing.digest()
						return tmp_answer



# 					print(m.hexdigest())

while True:

	data = s.recv(4096)
	if not data:
		break

	data_string = data.decode("utf-8")

	print data_string

	if 'What string' not in data_string:
		continue



	data_entries = data_string.strip().split()
	print data_entries
	begin_0 = data_entries[7][0:2]
	begin_1 = data_entries[8][0:2]
	begin_2 = data_entries[9][0:2]
	begin_3 = data_entries[10][0:2]

	print begin_0, begin_1, begin_2, begin_3


	print(data_string)


	code = make_answer(begin_0, begin_1, begin_2, begin_3)


	


	print(":".join("{:02x}".format(ord(c)) for c in code))

	s.send(code + '7\n')
	# s.send('5\n')


s.close()


	
		
		





