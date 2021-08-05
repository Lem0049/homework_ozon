shows = {
    'Секретные материалы': {'Жанр': 'фантастика', 'Рейтинг': 0.9},
    'Ведьмак': {'Жанр': 'фэнтази', 'Рейтинг': 0.95},
    'Клан Сопрано': {'Жанр': 'криминал', 'Рейтинг': '0.8'},
    '24': {'Genre': 'драма', 'Rating': 0.75},
    'Черное зеркало': {'Жанр': 'фантастика', 'Рейтинг': 0.98},
    'Во все тяжкие': {'Жанр': 'криминал', 'Рейтинг': '0.85'},
    'Игра престолов': {'Жанр': 'фэнтази', 'Рейтинг': 0.87},
    'Карточный домик': {'Genre': 'драма', 'Rating': 0.82},
    'Рик и Морти': {'Жанр': 'фантастика', 'Рейтинг': 1}
}

average = []
for i in shows.keys():
    try:
        if (shows[i]['Рейтинг']) > 0:
            average.append(float(shows[i]['Рейтинг']))
    except KeyError as k_e:
        print(f'KeyError    : {k_e}')
    except TypeError as t_e:
        print(f'TypeError   : {t_e}')
    try:
        if (shows[i]['Rating']) > 0:
            average.append(float(shows[i]['Rating']))
    except KeyError as k_e:
        print(f'KeyError    : {k_e}')
    except TypeError as t_e:
        print(f'TypeError   : {t_e}')

a = float(sum(average) / len(average))
print(a)

