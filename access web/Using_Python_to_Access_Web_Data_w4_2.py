# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Avsta.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags

tags = soup('a')
#print(soup)
required_count=0
required_position=18
count=0
position=0
str1=list()
str3=list()
for tag in tags:
    position=position+1
    if position==required_position:
        print('URL:', tag.get('href', None))
        url=tag.get('href', None)
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        position=0
        for tag in tags:
            position = position + 1
            if position == required_position:
                print('URL:', tag.get('href', None))
                url = tag.get('href', None)
                html = urllib.request.urlopen(url, context=ctx).read()
                soup = BeautifulSoup(html, 'html.parser')
                tags = soup('a')
                position = 0
                for tag in tags:
                    position = position + 1
                    if position == required_position:
                        print('URL:', tag.get('href', None))
                        url = tag.get('href', None)
                        html = urllib.request.urlopen(url, context=ctx).read()
                        soup = BeautifulSoup(html, 'html.parser')
                        tags = soup('a')
                        position = 0
                        for tag in tags:
                            position = position + 1
                            if position == required_position:
                                print('URL:', tag.get('href', None))
                                url = tag.get('href', None)
                                html = urllib.request.urlopen(url, context=ctx).read()
                                soup = BeautifulSoup(html, 'html.parser')
                                tags = soup('a')
                                position = 0
                                for tag in tags:
                                    position = position + 1
                                    if position == required_position:
                                        print('URL:', tag.get('href', None))
                                        url = tag.get('href', None)
                                        html = urllib.request.urlopen(url, context=ctx).read()
                                        soup = BeautifulSoup(html, 'html.parser')
                                        tags = soup('a')
                                        position = 0
                                        for tag in tags:
                                            position = position + 1
                                            if position == required_position:
                                                print('URL:', tag.get('href', None))
                                                url = tag.get('href', None)
                                                html = urllib.request.urlopen(url, context=ctx).read()
                                                soup = BeautifulSoup(html, 'html.parser')
                                                tags = soup('a')
                                                position = 0
                                                for tag in tags:
                                                    position = position + 1
                                                    if position == required_position:
                                                        print('URL:', tag.get('href', None))
                                                        print('Contents:', tag.contents[0])