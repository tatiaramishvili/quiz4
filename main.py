import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
payload={'page':'audios','send[shop.catalog][page]':1}
url='https://www.lit.ge/index.php'
file = open('books.csv', 'w', encoding='UTF-8-sig')
file_object=csv.writer(file)
file_object.writerow(['Names','Prices','Authors'])
while payload['send[shop.catalog][page]']<=17 :
    r = requests.get(url, params=payload)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    book_block = soup.find('section', class_='list-holder')
    books = book_block.find_all('article', class_='item-holder')
    for each in books:
        price = each.find('span', class_='price')
        price = price.text
        prices = price.replace(" ", "")
        name = each.find('div', class_='title-bar')
        book_names = name.a.text
        book = book_names.replace(',', '')
        author=each.span.b.text
        file_object.writerow([book,prices,author])
    payload['send[shop.catalog][page]']+=1
    sleep(10)
