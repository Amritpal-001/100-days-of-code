from bs4 import BeautifulSoup

import urllib.request
import shutil
import re

#Using Random ID generator
from fake_useragent import UserAgent
ua1 = UserAgent()
randomHeader = {'User-Agent':str(ua1.random)}
print(randomHeader)

#Extracting data from website
url = "https://www.flipkart.com/search?q=laptop&sid=4rr%2Ctz1&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_6_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CGaming+Laptops&requestId=7e139d13-db7e-4345-8bd8-83350c571253&as-searchtext=laptop"
import requests
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
aas = soup.find_all("div", class_='_3liAhj')


#FLIPKART terminologies
'''
_2cLu-l    - Product Name
_1vC4OE - Price

'''
prefix = '_2cLu-l" href="/'
suffix = '/'  
a = (('{prefix}(.+?){suffix}').format(prefix = prefix , suffix = suffix))
print(a)

#How to write a custom function for this????  - using variable inside a comma?
def Extractvalue(prefix , suffix  ,  inputvariable):
    value = re.search((('{prefix}(.+?){suffix}').format(prefix = prefix , suffix = suffix)), str(inputvariable))  #Search Values
    Name = value.group(1)
    print(Name)
    return(Name)

    
#Extracting specific values from data 
image_info = []
for a in aas:
    image_tag = a.findChildren("a")
    try:
        ProductName = Extractvalue( '_2cLu-l" href="/'      ,         '/'  ,  str(image_tag))
        DiscountedPrice  = Extractvalue( '_1vC4OE">'      ,         '<'  ,  str(image_tag))
        ActualPrice = Extractvalue( '_3auQ3N">₹<!-- -->'      ,         '<'  ,  str(image_tag))
        Discount = Extractvalue( 'VGWI6T"><span>'      ,         ' off'  ,  str(image_tag))
    except:
        print(image_tag , "has a missing value")
        
    #image_tag =  re.sub('/', '', image_tag)
    image_info.append(( ProductName, DiscountedPrice , ActualPrice,Discount))
  
a = image_info[1]
print(a[0])



#Sample Image_tag from flipkart
'''
'[<a class="Zhf2z-" href="/acer-nitro-5-core-i5-10th-gen-8-gb-1-tb-hdd-256-gb-ssd-windows-10-home-4-graphics-
nvidia-geforce-gtx-1650-an515-55-gaming-laptop/p/itm63d4da042e6b4?pid=COMFTBYVSHPY598R&amp;lid=LSTCOMFTBYVSH
PY598RBZLUOK&amp;marketplace=FLIPKART&amp;srno=s_1_40&amp;otracker=AS_QueryStore_HistoryAutoSuggest_1_6_na_na
_na&amp;otracker1=AS_QueryStore_HistoryAutoSuggest_1_6_na_na_na&amp;fm=organic&amp;iid=8a7129c5-b916-4c6b-96f9
-81a3bc4e32dc.COMFTBYVSHPY598R.SEARCH&amp;ssid=lukdjpwzhs0000001601060933661&amp;qH=312f91285e048e09" rel="noo
pener noreferrer" target="_blank">
<div><div><div class="_3BTv9X"
style="height:280px;width:200px">
<img alt="Acer Nitro 5 Core i5 10th Gen - (8 GB/1 TB HDD/256 GB SSD/Windows 10 Home/4 GB Graphics/NVIDIA Geforc
e GTX 1650) AN515-55 Gaming Laptop" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeh
older_9951d0.svg"/>
</div></div>
</div><div class="_3gDSOa _3iGnbq">
<div class="DsQ2eg">
<svg class="_2oLiqr" height="16" viewbox="0 0 20 16" width="16" xmlns="http://www.w3.org/2000/svg">
<path class="_35Y7Yo" d="M8.695 16.682C4.06 12.382 1 9.536 1 6.065 1 3.219 3.178 1 5.95 1c1.566 0 3.069.746
4.05 1.915C10.981 1.745 12.484 1 14.05 1 16.822 1 19 3.22 19 6.065c0 3.471-3.06 6.316-7.695 10.617L10 17.897
l-1.305-1.215z" fill="#2874F0" fill-rule="evenodd" opacity=".9" stroke="#FFF"></path></svg></div></div></a>,

<a class="_2cLu-l" href="/acer-nitro-5-core-i5-10th-gen-8-gb-1-tb-hdd-256-gb-ssd-windows-10-home-4-graphics-nvidia
-geforce-gtx-1650-an515-55-gaming-laptop/p/itm63d4da042e6b4?pid=COMFTBYVSHPY598R&amp;lid=LSTCOMFTBYVSHPY598RBZLUOK
&amp;marketplace=FLIPKART&amp;srno=s_1_40&amp;otracker=AS_QueryStore_HistoryAutoSuggest_1_6_na_na_na&amp;otracker1
=AS_QueryStore_HistoryAutoSuggest_1_6_na_na_na&amp;fm=organic&amp;iid=8a7129c5-b916-4c6b-96f9-81a3bc4e32dc.
COMFTBYVSHPY598R.SEARCH&amp;ssid=lukdjpwzhs0000001601060933661&amp;qH=312f91285e048e09" rel="noopener noreferrer"
target="_blank" title="Acer Nitro 5 Core i5 10th Gen - (8 GB/1 TB HDD/256 GB SSD/Windows 10 Home/4 GB Graphics/NVI
DIA Geforce GTX 1650) AN515-55 Gaming Laptop">Acer Nitro 5 Core i5 10th Gen - (8 GB/1 TB HDD/256 GB S...</a>,

<a class="_1Vfi6u" href="/acer-nitro-5-core-i5-10th-gen-8-gb-1-tb-hdd-256-gb-ssd-windows-10-home-4-graphics-nvidia-
geforce-gtx-1650-an515-55-gaming-laptop/p/itm63d4da042e6b4?pid=COMFTBYVSHPY598R&amp;lid=LSTCOMFTBYVSHPY598RBZLUOK&a
mp;marketplace=FLIPKART&amp;srno=s_1_40&amp;otracker=AS_QueryStore_HistoryAutoSuggest_1_6_na_na_na&amp;otracker1=AS
_QueryStore_HistoryAutoSuggest_1_6_na_na_na&amp;fm=organic&amp;iid=8a7129c5-b916-4c6b-96f9-81a3bc4e32dc.COMFTBYVSHPY
598R.SEARCH&amp;ssid=lukdjpwzhs0000001601060933661&amp;qH=312f91285e048e09" rel="noopener noreferrer" target="_blank"><div class="_1uv9Cb">


<div class="_1vC4OE">₹74,990</div>
<div class="_3auQ3N">₹<!-- -->89,990</div>
<div class="VGWI6T"><span>16% off</span></div></div></a>]'

'''
