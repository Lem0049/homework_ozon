from bs4 import BeautifulSoup
import requests
import re

req = requests.get('https://ru.wikipedia.org/wiki/Небьюла')
result = req.text
soup = BeautifulSoup(result, 'html.parser')
tet = soup.find_all('a', href=True)
item_list = [i.get('href', http=True) for i in tet]
print(item_list)
