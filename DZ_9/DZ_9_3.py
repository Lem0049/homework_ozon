import re

with open('cats of ultrah.txt', 'r', encoding='utf8') as file:
    cat_count = []
    for row in file.read().splitlines():
        result = re.findall(r"[Кк]ош\w{1,3}\b", row)
        if len(result) > 0:
            cat_count = cat_count + result

print(len(cat_count))
