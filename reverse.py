
import struct

byte_array = []
with open('text-083fea73abe439fcc2e1ebf51d3aa201.enc', 'rb') as f:
	while True:
		byte_s = f.read(1)
		if not byte_s:
			break

		byte = byte_s[0]

		# byte_array.append(struct.unpack('i', byte_s)[0])
		byte_array.append(byte)


print(byte_array)
print(len(byte_array))



import sys
import socket
import string
from subprocess import call




answer = []
i = len(byte_array)/4 - 1
while i >= 0:
	byte0_t = byte_array[i*4]
	byte1_t = byte_array[i*4+1]
	byte2_t = byte_array[i*4+2]
	byte3_t = byte_array[i*4+3]

	byte1 = ord(byte2_t) ^ ord(byte0_t)
	byte2 = ord(byte3_t) ^ ord(byte0_t)
	byte3 = ord(byte1_t) ^ byte1
	byte0 = byte1 ^ ord(byte3_t)

	answer.append(byte3) 
	answer.append(byte2) 
	answer.append(byte1) 
	answer.append(byte0) 

	if i > 0:
		byte_array[(i-1)*4] = chr(ord(byte_array[(i-1)*4]) ^ (byte0 ^ 0xFF))
		byte_array[(i-1)*4+1] = chr(ord(byte_array[(i-1)*4+1]) ^ (byte1 ^ 0xFF))
		byte_array[(i-1)*4+2] = chr(ord(byte_array[(i-1)*4+2]) ^ (byte2 ^ 0xFF))
		byte_array[(i-1)*4+3] = chr(ord(byte_array[(i-1)*4+3]) ^ (byte3 ^ 0xFF))


	i -= 1
answer.reverse()
for ch in answer:
	sys.stdout.write(chr(ch))
print ''


	





