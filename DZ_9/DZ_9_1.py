import re

z = []
with open('lesson09_closest_galaxies.csv', 'r', encoding='utf8') as i:
    s = i.readline()
    for s in i:
        spt = s.split(',')[0]
        z.append(re.split('[,;\n]', s))
        if re.search(r'Кит|Пегас|Рыбы', s):
            print(spt)
        if re.search(r'^[a-z,A-Z]', s):
            print(spt)
        if re.search(r'\d$', spt):
            print(spt)


print(z)
