# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
total=int(0)
lst=list()
# Retrieve all of the anchor tags
tags = soup('a')
# print(tags)

for tag in tags:
    tag=str(tag)
    count=re.findall('href="http://py4e-data.dr-chuck.net/known_by_(.+)"',tag)
    print(count)
#     number=int(count[0])
   
#     lst.append(number)
   
# print(lst)
# print(sum(lst))
