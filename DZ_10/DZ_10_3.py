# -*- coding: utf-8 -*-
import re

shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

fantastic_shows1 = {i : shows[i] for i in shows.keys() if re.match(r'ф[аэ]нта[зс]', shows[i]) is not None }
fantastic_shows = {serial: shows[serial] for serial in shows.keys() if shows[serial] == 'фантастика' or shows[serial] == 'фэнтази'}

print(fantastic_shows)
print(fantastic_shows1)
fantastic_shows_list = [f_serial for f_serial in fantastic_shows.keys()]
print(fantastic_shows_list)