import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url  = input('Enter URL// ')
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html,'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
    






    # url = 'https://www.wedo-digital.co.uk/'
# https://time.org.pk/