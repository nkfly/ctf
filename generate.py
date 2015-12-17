def gen(num):
	one = '$$/$$'
	two = '$$/$$ + $$/$$'
	three = '$$ - $$/$$'
	four = '$$'
	dic = {1:one, 2:two, 3:three, 4:three}
	

	index_64 = num / 64

	if num % 64 == 0:
		return '$$ ** $$ * ' []