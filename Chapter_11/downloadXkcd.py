#! /usr/bin/python3
#downloardXkcd.py - Downloads every single XKCD comic

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    #Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    #TODO Find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        #Download the image.
        print('Downloading the image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        #save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    #Get the prev button's URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')