import re

z = []
with open('lesson09_closest_galaxies.csv', 'r', encoding='utf8') as i:
    s = i.readline()
    for s in i:
        z.append(re.split('[,;\n]', s))
        if re.search(r'Кит|Пегас|Рыбы', s):
            print(s.split(',')[0])
        if re.search(r'^[a-z,A-Z]', s):
            print(s.split(',')[0])
        if re.search(r'\d$', s.split(',')[0]):
            print(s.split(',')[0])


print(z)
