import io

word = u'кошка'
i = 0
with io.open('lafcraft.txt', encoding='utf-8') as file:
    for line in file:
        if word in line:
            i = i + 1
            print(line)

print(i)
