anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
'''This program create list wit same genre for two different girls'''


def get_attraction(list1, list2):  # create function
    cross = list(set(list1.values()) & set(list2.values()))  # find crossing genre
    return print(cross)  # print list


get_attraction(anya, nastya)
get_attraction(olya, sveta)
get_attraction(sveta, anya)
