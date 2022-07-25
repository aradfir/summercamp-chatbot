import requests
from bs4 import BeautifulSoup
from os.path import join
def find_postings(category_link):
    category_req = requests.get(category_link)
    category_soup = BeautifulSoup(category_req.text, 'html.parser')
    listing=category_soup.find('div',{'class':'post-card-item'})
    for i in range(12):
        # print(listing.prettify())
        title=listing.find('h2',{'class':'kt-post-card__title'})
        print(title.text)
        if listing.find('picture') is None:
            print("No image")
        else:
            print("Image")
        if listing.find('i',{'class':'kt-icon-chat-bubble'}) is None:
            print('No chat')
        else:
            print("Has Chat")
        listing=listing.find_next('div',{'class':'post-card-item'})





BASE_URL = 'https://www.divar.ir/'
Tehran_URL = join(BASE_URL, 's/tehran')
req = requests.get(Tehran_URL)
soup = BeautifulSoup(req.text, 'html.parser')
categories = soup.find('ul', {'class': 'kt-accordion'})
print("CATEGORIES")
print(categories.get_text("\n", True))
for category_link in categories.find_all('a'):
    full_category_link = join(BASE_URL, category_link['href'][1:])
    print(full_category_link)
    find_postings(full_category_link)


# print(soup.prettify())
