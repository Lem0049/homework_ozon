# -*- coding: utf-8 -*-
import pickle

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


def genre_film(g_name):
    f_list = {}

    for i in shows.keys():
        try:
            if shows[i]['Жанр'] == g_name:
                f_list[i] = float(shows[i]['Рейтинг'])
        except KeyError as k_e:
            print(f'KeyError{k_e}')
        except TypeError as t_e:
            print(f'TypeError{t_e}')
        try:
            if shows[i]['Genre'] == g_name:
                f_list[i] = float(shows[i]['Rating'])
        except KeyError as k_e:
            print(f'KeyError{k_e}')
        except TypeError as t_e:
            print(f'TypeError{t_e}')

    average_final = sum(f_list.values()) / len(f_list.values())
    with open(f'{g_name.upper()}.dat', "wb") as f:
        pickle.dump(f_list, f)
    return f'в жанре {g_name} всего {len(f_list)} сериалов, средний рейтинг которых равен{average_final}'


list_genre = []
for key, value in shows.items():
    list_genre.append(list(shows[key].values())[0])
set_genre = set(list_genre)
for elem in set_genre:
    print(genre_film(elem))
