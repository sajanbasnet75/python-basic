import requests
from bs4 import BeautifulSoup
url="https://www.crummy.com/software/BeautifulSoup"
req=requests.get(url)
html_doc=req.text
soup=BeautifulSoup(html_doc, "html5lib")
pretty_soup=soup.prettify()

#print(pretty_soup)
print(soup.title)
print(soup.text)
a_tags=soup.find_all('a')
for link in a_tags:
    print(link.get('href'))
