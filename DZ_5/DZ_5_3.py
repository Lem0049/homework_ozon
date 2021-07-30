word = u'кошка '
c = []
with open('lafcraft.txt', encoding='utf-8') as file:
    for line in file:
        c.append(line.count(word))
        if word in line:
            print(line)

print(sum(c))
