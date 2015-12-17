from scipy import misc

import scipy.misc
import sys
lena_secret = misc.imread('stego.png')

print(type(lena_secret))
print(lena_secret.shape)
print(lena_secret.dtype)

# lenna = misc.imread('Lenna256x256.bmp')
# 
# print(type(lenna))
# print(lenna.shape)
# print(lenna.dtype)

channel = 2
for i in range(256):
	for j in range(0, 256, 8):
		# bits = (lena_secret[i][j][channel] % 2) * 128 + (lena_secret[i][j+1][channel] % 2) * 64 + (lena_secret[i][j+2][channel] % 2) * 32 + (lena_secret[i][j+3][channel] % 2) * 16 + (lena_secret[i][j+4][channel] % 2) * 8 + (lena_secret[i][j+5][channel] % 2) * 4 + (lena_secret[i][j+6][channel] % 2) * 2 + (lena_secret[i][j+7][channel] % 2) * 1
		bits = (lena_secret[i][j][channel] % 2) * 1 + (lena_secret[i][j+1][channel] % 2) * 2 + (lena_secret[i][j+2][channel] % 2) * 4 + (lena_secret[i][j+3][channel] % 2) * 8 + (lena_secret[i][j+4][channel] % 2) * 16 + (lena_secret[i][j+5][channel] % 2) * 32 + (lena_secret[i][j+6][channel] % 2) * 64 + (lena_secret[i][j+7][channel] % 2) * 128

		sys.stdout.write(chr(bits))
	sys.stdout.write('\n')



			
				# print(str(i) + ',' + str(j) + ',' + str(k) + ' lenna secret is ' + str(int(lena_secret[i][j][k])) + ' , lenna normal is ' + str(int(lenna[i][j][k])))
				# print(abs(lena_secret[i][j][k] - lenna[i][j][k]))