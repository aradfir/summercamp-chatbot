import requests
from bs4 import BeautifulSoup
URL ='https://www.divar.ir/s/tehran'
req=requests.get(URL)
soup = BeautifulSoup(req.text, 'html.parser')
categories=soup.find('ul',{'class':'kt-accordion'})
print("CATEGORIES")
print(categories.get_text("\n",True))
#print(soup.prettify())
