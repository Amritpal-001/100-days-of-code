from fake_useragent import UserAgent
'''
for i in range(10):
    ua2 = UserAgent()
    print(ua2.random)
'''
ua1 = UserAgent()
randomHeader = {'User-Agent':str(ua1.random)}

import requests
scrapeLink = 'https://en.wikipedia.org/wiki/Megacity'
page = requests.get(scrapeLink, randomHeader)


from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

megaTable = soup.find_all('table')[1]
