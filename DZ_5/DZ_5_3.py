word = u'кошка '
total_word = 0
with open('lafcraft.txt', encoding='utf-8') as file:
    for line in file:
        word_count = line.count(word)
        if word_count > 0:
            total_word = total_word + word_count
            print(line)

print(total_word)
