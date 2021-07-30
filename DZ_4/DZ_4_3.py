shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}

"""this program is calculates average rating for films of the same genre"""


# def get_value(dictionary, value):
#     clue = []
#     for k, v in dictionary.items():
#         if v == value:
#             clue.append(k)
#     return clue
def get_value(value):
    film_collection = [k for k, v in shows.items() if v == value]  # sort film by genre
    rating_coll = []  # create empty  list
    for i in film_collection:  # condition for sort Film by rating
        rating_coll.append(ratings[i])  # append rating in list
    return float(sum(rating_coll)) / len(rating_coll)  # calculates average of rating


genre = input('Введите жанр фильма  :')  # input genre
print(get_value(f'{genre}'))  # print average
