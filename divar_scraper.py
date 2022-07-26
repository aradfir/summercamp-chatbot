import requests
from bs4 import BeautifulSoup
from os.path import join

MAX_ITEMS_PER_CATEGORY = 12
BASE_URL = 'https://www.divar.ir/'


def find_postings(category_link):
    category_req = requests.get(category_link)
    category_soup = BeautifulSoup(category_req.text, 'html.parser')
    listing = category_soup.find('div', {'class': 'post-card-item'})
    for i in range(MAX_ITEMS_PER_CATEGORY):
        title = listing.find('h2', {'class': 'kt-post-card__title'})
        print(title.text)
        if listing.find('picture') is None:
            print("Listing contains image")
        else:
            print("This listing does not contain an image")

        if listing.find('i', {'class': 'kt-icon-chat-bubble'}) is not None:
            print("Chat functionality is available for this ad")
        else:
            print('Chat functionality is disabled for this ad')

        listing = listing.find_next('div', {'class': 'post-card-item'})


if __name__=='__main__':
    Tehran_URL = join(BASE_URL, 's/tehran')
    req = requests.get(Tehran_URL)
    soup = BeautifulSoup(req.text, 'html.parser')
    categories = soup.find('ul', {'class': 'kt-accordion'})
    print("=====CATEGORIES=====")
    print(categories.get_text("\n", True))
    for link in categories.find_all('a'):
        full_category_link = join(BASE_URL, link['href'][1:])
        print(full_category_link)
        find_postings(full_category_link)


