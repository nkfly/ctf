import requests


session = requests.Session()
long_text = 'a'*345 + 'b'*32
long_password = 'b' * 32
# 346, 378
params = {'locale' : "en"}
print 'e'
r = session.get("http://www.journalism.ntu.edu.tw", params=params)
print '2'
# print session.cookies.get_dict()
# r = requests.get("http://54.92.88.102/cgi-bin/nanana")


print r.status_code
print r.headers
print r.content
# print r.cookies['auth']
