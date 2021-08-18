from bs4 import BeautifulSoup
import requests

req = requests.get('https://store.steampowered.com/genre/Free%20to%20Play/')
result = req.text
soup = BeautifulSoup(result, 'html.parser')
tet = soup.find_all('a')

codename = "Free To Play"
item_list = []
for it in tet:
    item_text = it.text
    item_url = it.get('href')
    item_list.extend([item_text, item_url])
final_dict = {}
for index in range(len(item_list)):
    if codename in item_list[index]:
        final_dict |= {item_list[index + 1]: item_list[index]}
print(final_dict)
