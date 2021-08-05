"""This program counts the number of words in a file"""

word = u'кошка '  # Set variable
total_word = 0  # Set counter
with open('lafcraft.txt', encoding='utf-8') as file:  # Open file
    for line in file:  # Set cycle for searching line in file
        word_count = line.count(word)  # How many times does the word cat appear
        if word_count > 0:  # Set cycle for counter
            total_word = total_word + word_count  # Count word
            print(line)     # Print line with world

print(total_word)   # Print counter
