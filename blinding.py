import requests
from pwn import *

import gmpy
import sys
import socket
import string
from subprocess import call

import base64
import string




n = 29483112906907846550407371381907804051925957834404110624325531950200215274674279351500117069061279396866776918114198748748643519779529947303729199772247349
c = 0x1c9d992fd1c6c9f26b24fb127e3e1ac343eadb0dad36c27747111ad07238bf9bc76d16737f8f7fc6752df563027fc6614a8c803de38bbe6aefca0e7f3ec739ba4

sen = pow(2, 65537, n) * c
# sen = 2 ** 65537 * c
print(gmpy.invert(17, 3120))




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("csie.ctf.tw", 10119))


print (str(c))
s.send( str(sen) + '\n')

data = s.recv(4096)


s.close()
data_string = str(data)

sys.stdout.write('data: ' + data_string)

ans = (int(data_string) * gmpy.invert(2, n)) % n

print (hex(ans)[2:]).decode('hex')


