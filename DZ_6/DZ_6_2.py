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
'''This function create .dat file with list of film same genre.'''


def genre_film(g_name): # start function
    f_list = {}     # empty dict

    for i in shows.keys():      # start cycle
        try:
            if shows[i]['Жанр'] == g_name:  # search value for key"Жанр" in dictionary
                f_list[i] = float(shows[i]['Рейтинг'])
        except KeyError as k_e:
            print(f'KeyError{k_e}')
        except TypeError as t_e:
            print(f'TypeError{t_e}')
        try:
            if shows[i]['Genre'] == g_name:     # search value for key"Genre" in dictionary
                f_list[i] = float(shows[i]['Rating'])
        except KeyError as k_e:
            print(f'KeyError{k_e}')
        except TypeError as t_e:
            print(f'TypeError{t_e}')

    average_final = sum(f_list.values()) / len(f_list.values())     # calculate average rating for film same genre
    with open(f'{g_name.upper()}.dat', "wb") as f:  # create file
        pickle.dump(f_list, f)
    return f'в жанре {g_name} всего {len(f_list)} сериалов, средний рейтинг которых равен{average_final}' # return
    # result


list_genre = []
for key, value in shows.items():
    list_genre.append(list(shows[key].values())[0])
set_genre = set(list_genre)
for elem in set_genre:
    print(genre_film(elem))
