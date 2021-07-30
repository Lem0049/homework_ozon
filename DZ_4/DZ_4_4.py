import random

ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}
shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

'''This program give you random choice film with rating => 0.85'''

top_rating = 0.85

best_films = [k for k, top_rating in ratings.items() if
              top_rating >= 0.85]  # create list of best films, with rating => 0.85

active = True  # variable for break
while active:
    film_f_ev = random.choice(best_films)  # random choice film
    genre_f = shows[film_f_ev]  # genre of random film
    print(f'Ваш фильм на вечер {film_f_ev} в жанре {genre_f}')  # print film with genre
    choice = input(f'Вам нравится наш выбор?(да или нет)')  # ask user about our choice
    while choice != 'да' and choice != 'нет':  # test answer
        print('Введите да или нет')
        choice = input(f'Вам нравится наш выбор?(да или нет)')
    if choice == 'да':  # if user like our choice then have a nice day
        print('Приятного просмотра')
        active = False
    else:  # if not try again
        continue
