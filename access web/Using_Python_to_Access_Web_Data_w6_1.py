import json
from urllib.request import urlopen
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'http://py4e-data.dr-chuck.net/comments_1616319.json'
if address == '':
    quit()
data = urlopen(address).read()

# unpack JSON
data = json.loads(data)

total = 0
for user in data['comments']:
    total = total + user['count']

print('Total comments:', total)