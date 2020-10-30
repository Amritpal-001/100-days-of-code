from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil

import re

url = "https://en.wikipedia.org/wiki/Richard_Feynman"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

aas = soup.find_all("a", class_='image')


image_info = []

for a in aas:
    image_tag = a.findChildren("img")
    #image_tag =  re.sub('/', '', image_tag)
    image_info.append((re.sub('//', 'https://', image_tag[0]["src"]), image_tag[0]["alt"]))
    #image_info.append((image_tag[0]["src"], image_tag[0]["alt"]))


a = image_info[1]
print(a[0])


#repacing any symbol with another
string = '//upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Richard_Feynman_signature.svg/150px-Richard_Feynman_signature.svg.png'
print(re.sub('//', 'abc', string))




def download_image(image):
    response = requests.get(image[0], stream=True)
    realname = ''.join(e for e in image[1] if e.isalnum())
    
    file = open("/data/{}.jpg".format(realname), 'wb')
    
    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response


for i in range(0, len(image_info)):
    download_image(image_info[i])

