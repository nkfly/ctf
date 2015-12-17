import requests
from pwn import *


import sys
import socket
import string
from subprocess import call

import base64
import string

import signal
import os
import time
import random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256


class MyAES:

	def __init__(self, key):
		self.key = key
		self.iv = 'This is an IVIVI'

	def encrypt(self, raw):
		message = pad(raw)
		aes = AES.new(self.key, AES.MODE_CBC, self.iv)
		return base64.b64encode(aes.encrypt(message))

	def decrypt(self, enc):
		cipher = base64.b64decode(enc)
		aes = AES.new(self.key, AES.MODE_CBC, self.iv)
		return unpad(aes.decrypt(cipher))


def connect_until_step2(message):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("csie.ctf.tw", 10121))

	data = s.recv(4096)
	if not data:
		exit(0)

	data_string = str(data)
	print data_string

	time.sleep(6)
	data = s.recv(4096)
	if not data:
		exit(0)

	data_string = str(data)
	print data_string

	sha256 = SHA256.new()
	sha256.update(message)
	s.send( message + '||' + base64.b64encode(sha256.digest()) + '\n')


	data = s.recv(4096)
	if not data:
		exit(0)

	step_2data_string = str(data)
	print step_2data_string

	data = s.recv(4096)
	if not data:
		exit(0)

	data_string = str(data)
	print data_string
	return s, step_2data_string

s , step_2data_string = connect_until_step2('admin||helloworld')

print step_2data_string

ss , ss_step_2data_string = connect_until_step2('admin||' + step_2data_string.split('||')[0])
ss.close()

message = ss_step_2data_string.split('||')[1]
sha256 = SHA256.new()
sha256.update(message)
s.send( message + '||' + base64.b64encode(sha256.digest()) + '\n')

data = s.recv(4096)
if not data:
	exit(0)

data_string = str(data)
print data_string

data = s.recv(4096)
if not data:
	exit(0)

data_string = str(data)
print data_string

s.close()

