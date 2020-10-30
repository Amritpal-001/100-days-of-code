from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil

import re

url = "https://www.mamc.ac.in/mamc-biochemistry-faculity"
#url = "https://www.mamc.ac.in/mamc-community-medicine-faculty"

#url = "https://www.mamc.ac.in/mamc-pharmacology-faculty"

url = "https://www.mamc.ac.in/mamc-anatomyfaculty"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
aas = soup.find_all("div", class_='img-box')

image_info = []
for a in aas:
    image_tag = a.findChildren("img")
    #image_tag =  re.sub('/', '', image_tag)
    #image_info.append((re.sub('//', 'https://', image_tag[0]["src"]), image_tag[0]["alt"]))
    image_info.append((image_tag[0]["src"], image_tag[0]["alt"]))
a = image_info[1]
print(a[0])


def download_image(image):
    response = requests.get(image[0], stream=True)
    
    realname = ''.join(e for e in image[0] if e.isalnum())
    #print(realname)

    #/dr_surabhi_wadhwa.jpg
    realname1 = re.search('layoutimage(.+?).jpg', realname)
    #print(realname1[1])
    
    file = open("/home/amritpal/Downloads/Tensorflow certification - 100 days of code/Github/Code/Day1 - Web scrapping/MamcDataScrapped/{}.jpg".format(realname1[1]), 'wb')
    print("downloading" , realname1[1])
    
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response

for i in range(0, len(image_info)):
    download_image(image_info[i])

'''
import re

text = 'gfgfdAAA1234ZZZuijjk'

m = re.search('AAA(.+?)ZZZ', text)
if m:
    found = m.group(1)


    '''
