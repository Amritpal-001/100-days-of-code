import requests
from urllib.request import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama

# init the colorama module
colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET

# initialize the set of links (unique links)
internal_urls = set()
DownloadableUrls = []
external_urls = set()

total_urls_visited = 0


def is_valid(url):
    """ Checks whether `url` is a valid URL """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url):
    """ Returns all URLs that is found on `url` in which it belongs to the same website  """
    urls = set()
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)
        #print(href)
        parsed_href = urlparse(href) # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        #print(href)
        if not is_valid(href): # not a valid URL
            continue
        if href in internal_urls: # already in the set
            continue
        urls.add(href)
        #print(urls)
        if 'details' in href:
            internal_urls.add(href)
        if 'pdf' in href:
            if 'archive.org' in href:
                if 'download' in href:
                    if href not in DownloadableUrls:
                        DownloadableUrls.append(href)
                        print(href)
                   # print(f"{GREEN}[*] Internal link: {href}")
    #print('With details - ' ,internal_urls)
    print('Downloadable urls  - ' , DownloadableUrls)
    return urls


def crawl(url, max_urls=0):
    """ Crawls a web page , extracts all links.
     max_urls (int): number of max urls to crawl, default is 30  """
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url)
    #print(links)
    #print()
    print('Downloadable urls  - ' , DownloadableUrls)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)

webaddress = 'https://archive.org/details/abroadcranethoma00craniala/page/n4/mode/2up'
crawl(webaddress)
print(internal_urls)

'''
if __name__ == "__main__":
    #webaddress = input('Enter web address')
    for n in range (0 , len(internal_urls)):
        
    webaddress = 'https://archive.org/details/abroadcranethoma00craniala/page/n4/mode/2up'
    crawl(webaddress)
    '''
'''
https://www.pdfdrive.com/living-in-the-light-a-guide-to-personal-transformation-e10172273.html
https://www.pdfdrive.com/living-in-the-light-a-guide-to-personal-transformation-d10172273.html
https://archive.org/details/books
https://archive.org/details/tucows_8176_Doom
'''
