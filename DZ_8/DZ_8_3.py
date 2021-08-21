from bs4 import BeautifulSoup
import requests

req = requests.get('https://store.steampowered.com/genre/Free%20to%20Play/')
result = req.text
soup = BeautifulSoup(result, 'html.parser')
tab = soup.find_all('div', class_='tab_item_content')
game_genre ={}
for g_name in tab:
    key = g_name.find(class_='tab_item_name').text
    value = [v.text for v in g_name.find_all(class_='top_tag')]
    game_genre[key] = value

print(game_genre)


# count = [c.text for c in (soup.find_all('span', class_='tag_count tab_filter_control_count'))]
# genre = [g.text for g in (soup.find_all('span', class_='tag_name'))]
#
# genre_dict = {}
#
# for i in range(len(count)):
#     genre_dict |= {genre[i]: count[i]}
#
# print(genre_dict)
