import requests
from pwn import *


import sys
import socket
import string
from subprocess import call

import base64
import string



# FLAG{it's pudd1n6 0r4cl3! (dance) (hungry)}\x05\x05\x05\x05\x05

cipherBytes = base64.b64decode('NfHBHcVs1MzChTWg/yPibl97EcV9e566VfocKI60xhOVG/ko1PVQ2g9F5etdzLiAwPhczk8zPqJ99ohkKWehVg==')
print(len(cipherBytes))


blockSize = 16


ivIntermediate = ''
while len(ivIntermediate) < 16:

	for i in range(1,256):
		print('trying ' + str(i))
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("csie.ctf.tw", 10118))


		padding = ''
		for j in range(1, len(ivIntermediate)+1):
			padding += chr(ord(ivIntermediate[j-1]) ^ (len(ivIntermediate) + 1))
		padding = padding[::-1]

		
		tmpCipherBytes = '\x00' * (blockSize - len(ivIntermediate) - 1 ) + chr(i) + padding + cipherBytes[48:64]
		# tmpCipherBytes = cipherBytes[0:32]
		print ((tmpCipherBytes), len(tmpCipherBytes))


		tmpCipherBytes = base64.b64encode(tmpCipherBytes)
		
		s.send( tmpCipherBytes + '\n')

		data = s.recv(4096)
		if not data:
			break


		s.close()
		data_string = str(data)

		sys.stdout.write('data string ' + data_string)

		if 'true' in data_string:
			print 'found ' + str(i)

			ivIntermediate += chr(i ^ (len(ivIntermediate) + 1))
			break
			# break

			


ivIntermediate = ivIntermediate[::-1]
print 'ivIntermediate is ' + ivIntermediate

print(ivIntermediate, len(ivIntermediate))



firstBlock = ''
for i in range(16):

	firstBlock += chr(ord(ivIntermediate[i]) ^ ord(cipherBytes[i+32]))

print 'first block is ' + firstBlock


# ivIndex = 15
# while ivIndex >= 0:
# 	for i in range(256):
# 		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 		s.connect(("csie.ctf.tw", 10118))

# 		tmpCipherBytes = str(cipherBytes)
# 		tmpCipherBytes[ivIndex] = chr(i)

# 		s.send( tmpCipherBytes + '\n')

# 		data = s.recv(4096)
# 		if not data:
# 			break


# 		s.close()
# 		data_string = str(data)

# 		if 'true' not in data_string:

# 			break

		

# 	ivIndex -= 1



