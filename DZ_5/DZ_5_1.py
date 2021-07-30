anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}


def get_attraction(list1, list2):
    cross = list(set(list1.values()) & set(list2.values()))
    return print(cross)


get_attraction(anya, nastya)
get_attraction(olya, sveta)
get_attraction(sveta, anya)

