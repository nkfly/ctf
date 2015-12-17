import requests
from pwn import *


import sys
import socket
import string
from subprocess import call

import base64
import string


def try_block_size(cookie):
	startGarbage = 1
	blockSize = 16

	while True:
		tempCookie = cookie[startGarbage:]

		if tempCookie[0:blockSize] == tempCookie[blockSize:blockSize*2]:
			print('startGarbage', startGarbage)
			print('block size is ' + str(blockSize))
			print(tempCookie[0:blockSize],tempCookie[blockSize:blockSize*2])
			break


		startGarbage += 1
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("csie.ctf.tw", 10117))

# iter = 1
# while True:

# 	data = s.recv(4096)
# 	if not data:
# 		break

# 	data_string = str(data)
	


# 	if iter == 1:
# 		s.send( 'A'*1 + '\n')
# 	if iter == 2:
# 		# print 'try ' + 'A'*(13 + 16 + 16 - globalIter) + try_string + printable_c
# 		s.send( 'A'*(13 + 15) + ',' + 'A'*15 + '\n')

# 	if iter == 3:
# 		data_string = data_string[8:]
# 		start_string = base64.b64decode(data_string)
# 		try_block_size(start_string)

# 		break

# 	iter += 1
# s.close()



printables = string.printable
start_string = None
try_string = ''
globalIter = 1
while True:
	iter = 1
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("csie.ctf.tw", 10117))
	
	while True:

		data = s.recv(4096)
		if not data:
			break

		data_string = str(data)
		


		if iter == 1:
			s.send( 'A'*1 + '\n')
		if iter == 2:
			# print 'try ' + 'A'*(13 + 16 + 16 - globalIter) + try_string + printable_c
			s.send( 'A'*(13 + 16 + 16 - globalIter) + '\n')

		if iter == 3:
			data_string = data_string[8:]
			start_string = base64.b64decode(data_string)

			break

		iter += 1
	s.close()
	print 'iter ' + str(globalIter) + '  ' + start_string
	for printable_c in printables:	
		iter = 1

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("csie.ctf.tw", 10117))
		
		while True:

			data = s.recv(4096)
			if not data:
				break

			data_string = str(data)
			


			if iter == 1:
				s.send( 'A'*1 + '\n')
			if iter == 2:
				print 'try ' + 'A'*(13 + 16 + 16 - globalIter) + try_string + printable_c
				s.send( 'A'*(13 + 16 + 16 - globalIter) + try_string + printable_c + '\n')

			if iter == 3:
				data_string = data_string[8:]
				data_string = base64.b64decode(data_string)

				break

			iter += 1
		s.close()
		# print 'data_string is ' + data_string
		if data_string[0:64] == start_string[0:64]:
			try_string += printable_c
			break

	print (try_string)
	globalIter += 1




	









