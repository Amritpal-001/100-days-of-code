from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil

import re

url = "https://www.mamc.ac.in/mamc-biochemistry-faculity"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
aas = soup.find_all("div", class_='menu-shortcodes-column-1-container')

#print(aas)

image_info = []

for a in aas:
    image_tag = a.findChildren("a")
    image_tag = re.search('>(.+?)<', str(image_tag))
    
    #print(image_tag1 , image_tag)
    #print()
    image_tag =  re.sub('<', '', str(image_tag))    #replace text with something else
    image_tag =  re.sub('>', '', str(image_tag))    #replace text with something else
    
    image_tag = re.search("'(.+?)'", str(image_tag))
    #print(str(image_tag[1]))
    if str(image_tag[1]) not in image_info:
        image_info.append(str(image_tag[1]))
    
a = image_info
print(a)


'''
def download_image(image):
    response = requests.get(image[0], stream=True)
    print("downloading" , image[0])
    realname = ''.join(e for e in image[0] if e.isalnum())
    
    file = open("/home/amritpal/Downloads/Tensorflow certification - 100 days of code/Github/Code/Day1 - Web scrapping/MamcDataScrapped/{}.jpg".format(realname), 'wb')
    
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response

for i in range(0, len(image_info)):
    download_image(image_info[i])

import re

text = 'gfgfdAAA1234ZZZuijjk'

>Anatomy</a>

m = re.search('AAA(.+?)ZZZ', text)


text = 'gfgfdAAA1234ZZZuijjk'
>Anatomy</a>
m = re.search('>(.+?)</a>', text)


if m:
    found = m.group(1)
'''
