import sys

encoded = 'Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh'
before = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
after = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

for ch in encoded:
	if after.find(ch) == -1:
		sys.stdout.write(ch)
	else:
		sys.stdout.write(before[after.index(ch)])

print('')

# for ch in encoded:
	# sys.stdout.write(chr(ord(ch) + 13))
