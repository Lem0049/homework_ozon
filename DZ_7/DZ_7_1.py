animals = ['питон', 'питон', 'кит', 'собака', 'питон', 'кит', 'кошка', 'горилла', 'кит', 'кошка', 'жираф', 'леопард',
           'жираф', 'жираф', 'кошка', 'горилла', 'жираф', 'жираф', 'кошка', 'жираф', 'кошка', 'кошка', 'собака', 'кит',
           'жираф', 'леопард', 'жираф', 'собака', 'кит', 'кит', 'кит', 'жираф', 'собака', 'собака', 'кит', 'питон',
           'леопард', 'кошка', 'жираф', 'собака', 'кошка', 'жираф', 'кошка', 'собака', 'кит', 'леопард', 'леопард',
           'горилла',
           'горилла', 'кит']


def ind_find(index):
    ind_list = [i for i in range(len(animals)) if animals[i] == index]
    return ind_list


unic_animals = set(animals)
for pet in unic_animals:
    print(f'{pet}  :', ind_find(pet))
