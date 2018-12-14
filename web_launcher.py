from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser
import re

page = urlopen('https://www.alexa.com/topsites')
soup = BeautifulSoup(page, 'html.parser')
#site_box = soup.find('a', attrs={'class': ''})
#site = name_box.text.strip()

count = 0 
sites = []
for link in soup.find_all('a'):
    site = str(link.get('href'))
    if site.startswith('/siteinfo/'):
        count += 1 
        siteName = site
        siteName = re.sub('/siteinfo/', '', siteName)
        sites.append('http://www.' + siteName)
        print(('%d: ' +  siteName) % (count))


print('\n')

choice = int(input('Choose a number to open a site: '))

webbrowser.open_new_tab(sites[choice-1])