import re

with open('cats of ultrah.txt', 'r', encoding='utf8') as file:
    z = []
    for row in file.read().splitlines():
        result = re.findall(r' кошк| Кошк| коше| кот | Кот ', row)
        if len(result) > 0:
            z = z + result

print(len(z))
