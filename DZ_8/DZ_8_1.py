from bs4 import BeautifulSoup
import requests


req = requests.get('https://store.steampowered.com/genre/Free%20to%20Play/')
result = req.text
soup = BeautifulSoup(result, 'html.parser')
print(soup.find_all('a href'))