import re

z = []
with open('lesson09_closest_galaxies.csv', 'r', encoding='utf8') as i:
    s = i.readline()
    for s in i:
        spt = s.split(',')
        if re.search(r'Андромед', s):
            galaxy_dict = {'Название': f'{spt[0]}', 'Расстояние': f'{float("{0:.3}".format(spt[2]))}',
                           'Примечание': f'{spt[3]}'}
            z.append(galaxy_dict)

print(z)
for i in range(len(z)):
    min_i = i
    for j in range(i + 1, len(z)):
        if z[min_i]['Расстояние'] > z[j]['Расстояние']: min_i = j
    z[i], z[min_i] = z[min_i], z[i]

print(z)
