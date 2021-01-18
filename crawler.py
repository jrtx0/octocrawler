# -*- coding: utf-8 -*-

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

def img_urls():
    soup = urlopen('https://octodex.github.com')
    content = BeautifulSoup(soup.read(), 'html.parser')
    img_urls = []
    for link in content.find_all('img'):        
        if link.get('data-src') != None:
            img_urls.append('https://octodex.github.com' + link.get('data-src'))
    return img_urls

def img_names():
    soup = urlopen('https://octodex.github.com')
    content = BeautifulSoup(soup.read(), 'html.parser')
    img_names = []
    for link in content.find_all('a', attrs = {'class' : 'link-gray-dark text-bold'}):
        if link.string != None:
            img_names.append(link.string.strip())
    return img_names

def img_download():
    urls = img_urls()
    names = img_names()
    i = 0
    for url in urls:
        urlretrieve(url, './Octodex/' + names[i] + '.jpg')
        i += 1

if __name__ == '__main__':
    img_download()
