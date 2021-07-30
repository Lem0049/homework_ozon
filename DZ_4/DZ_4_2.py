anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

top_anya = set(anya)

if len(top_anya.intersection(olya.keys(), top_anya)) > len(top_anya.intersection(nastya.keys(), top_anya)) > len(top_anya.intersection(sveta.keys(), top_anya)):
    print(f'С Олей можно обсудить{len(top_anya.intersection(olya.keys(), top_anya))} сериала')
elif len(top_anya.intersection(nastya.keys(), top_anya)) > len(top_anya.intersection(sveta.keys(), top_anya)) > len(top_anya.intersection(olya.keys(), top_anya)):
    print(f'С Настей можно обсудить {len(top_anya.intersection(nastya.keys(), top_anya))} сериала')
else:
    print(f'Со Светой можно обсудить {len(top_anya.intersection(sveta.keys(), top_anya))} сериала')
