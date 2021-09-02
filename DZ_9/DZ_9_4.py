from bs4 import BeautifulSoup
import requests
import re

req = requests.get('https://ru.wikipedia.org/wiki/Небьюла')
result = req.text
soup = BeautifulSoup(result, 'html.parser')
tet = soup.find_all('a', href=re.compile(r'^http'))
wiki = soup.find_all('a', href=re.compile(r'https?://\w+.wiki\w+'))
item_list = set([i.get('href') for i in tet])
wiki_list = set([z.get('href') for z in wiki])
final_list = item_list - wiki_list      # item_list.difference(wiki_list)
print(wiki_list)
print(item_list)
print(final_list)