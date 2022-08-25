import json
import requests
from bs4 import BeautifulSoup

# with open('auction_prices.json', 'r', encoding='utf-8') as file:
#     file = json.load(file)

# for i in file:
# i = '25115'
# res = requests.get(f'https://www.wowhead.com/item={i}&xml').text
# soup = BeautifulSoup(res, 'xml')
#
# print(soup.find('json').text)

with open('auction_prices.json', 'r', encoding='utf-8') as file:
    file = json.load(file)

# i = file['25115']
i = 25115

res = requests.get(f'https://www.wowhead.com/wotlk/ru/item={i}').text
soup = BeautifulSoup(res, 'lxml')
soup = soup.find('script', type='text/javascript')
print(soup)
