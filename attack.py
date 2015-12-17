import requests


session = requests.Session()
long_text = 'a'*345 + 'b'*32
long_password = 'b' * 32
# 346, 378
# params = {'username' : long_text, 'password' : long_password, 'action' : 'login'}

r = session.get("http://www.theclipo.com/loginjj")
# print session.cookies.get_dict()
# r = requests.get("http://54.92.88.102/cgi-bin/nanana")


print r.status_code
print r.headers
# print r.content
# print r.cookies['auth']
