#https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-8.php


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)')

#html = urlopen('https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-8.php')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
#print(images)

for image in images: 
    print(image['src']+'\n')
